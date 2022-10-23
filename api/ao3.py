from typing import List

from AO3 import Session
from AO3 import Work as AO3_Work
from AO3.utils import workid_from_url
from django.conf import settings

from works.models import Author, Work


def get_ao3_session() -> Session:
    """
    Returns an AO3 Session object
    """
    return Session(settings.AO3_USERNAME, settings.AO3_PASSWORD)


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
        if counter > 1:
            break
        ao3_work = get_work(bookmark.url)
        ao3_author = ao3_work.authors[0]

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
                "complete": ao3_work.complete,
                "word_count": ao3_work.words,
                "date_published": ao3_work.date_published,
                "date_updated": ao3_work.date_edited,
                "metdata": ao3_work.metadata
            },
        )
        counter += 1

    print(f"{counter} works imported")
