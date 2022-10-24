from typing import List

from AO3 import Session
from AO3 import Work as AO3_Work
from AO3.threadable import threadable
from AO3.users import User as AO3_User
from AO3.utils import workid_from_url
from django.conf import settings

from works.models import Author, Work


class CustomSession(Session):
    @threadable
    def _load_bookmarks(self, page=1):
        """
        Override the default load_bookmarks method to add the ability to get
        "recommended" status
        """
        url = self._bookmarks_url.format(self.username, page)
        soup = self.request(url)
        bookmarks = soup.find("ol", {"class": "bookmark index group"})
        for bookm in bookmarks.find_all(
            "li", {"class": ["bookmark", "index", "group"]}
        ):
            authors = []
            recommended = False
            workid = -1
            if bookm.h4 is not None:
                # Get the author and work ID
                for a in bookm.h4.find_all("a"):
                    if "rel" in a.attrs.keys():
                        if "author" in a["rel"]:
                            authors.append(AO3_User(str(a.string), load=False))
                    elif a.attrs["href"].startswith("/works"):
                        workname = str(a.string)
                        workid = workid_from_url(a["href"])

                # Get whether the bookmark is recommended
                for span in bookm.p.find_all("span"):
                    if "title" in span.attrs.keys():
                        if span["title"] == "Rec":
                            recommended = True

                if workid != -1:
                    new = AO3_Work(workid, load=False)
                    setattr(new, "title", workname)
                    setattr(new, "authors", authors)
                    setattr(new, "recommended", recommended)
                    if new not in self._bookmarks:
                        self._bookmarks.append(new)


def get_ao3_session() -> Session:
    """
    Returns an AO3 Session object
    """
    return CustomSession(settings.AO3_USERNAME, settings.AO3_PASSWORD)


def get_bookmarks(session: Session) -> list:
    """
    Returns a list of ao3 Work objects.

    Included work fields:
    - url
    - title
    - authors (list of ao3 User objects)
        - url
        - username

    Note: A lot of the "work" fields are not loaded or for whatever
    reason do not seem to work with the get_bookmarks method.
    """
    return session.get_bookmarks()


def get_work(work_url: str) -> AO3_Work:
    """
    Returns an AO3 Work object

    Fields:
    - metadata: JSON field of everything
    - authors (list of ao3 User objects)
    - categories
    - complete
    - id
    - title
    - summary

    Note: Fields that don't work in get_bookmarks() work here!
    """
    work_id = workid_from_url(work_url)
    work = AO3_Work(work_id)
    return work


def import_bookmarks() -> List[AO3_Work]:
    """
    Retrieves all AO3 bookmarks, and loads them into the DB
    """
    session = get_ao3_session()
    bookmarks = get_bookmarks(session)

    counter = 0

    for bookmark in bookmarks:
        ao3_work = get_work(bookmark.url)
        ao3_author = ao3_work.authors[0]

        # Note: If the work is "recommended," we make the assumption that the user
        # has also read it and mark the status as READ.
        if bookmark.recommended:
            status = Work.Status.READ
        else:
            status = Work.Status.TBR

        # At this point, only gets first author
        author, _ = Author.objects.get_or_create(
            url=ao3_author.url, defaults={"username": ao3_author.username}
        )
        work, _ = Work.objects.update_or_create(
            url=ao3_work.url,
            defaults={
                "platform_id": ao3_work.id,
                "author": author,
                "title": ao3_work.title,
                "summary": ao3_work.summary,
                "status": status,
                "complete": ao3_work.complete,
                "word_count": ao3_work.words,
                "date_published": ao3_work.date_published,
                "date_updated": ao3_work.date_edited,
                "metadata": ao3_work.metadata,
            },
        )
        counter += 1

    print(f"{counter} works imported")
