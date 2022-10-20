from unittest.mock import patch
from AO3 import Session

from api.ao3 import get_ao3_session


def test_get_ao3_session():
    with patch.object(Session, "__init__", return_value=None):
        session = get_ao3_session()
        assert isinstance(session, Session)


def test_get_bookmarks():
    """
    FIXME: How to mock these kinds of classes? Idea:

    - import responses
    @responses.activate

    # Add the request that would get the authenticity token
    responses.add(responses.GET, "https://archiveofourown.org/users/login", json={}, status=200)

    # Add the login response
    responses.add(responses.POST, self.url, json={}, status=302)
        - url = "https://archiveofourown.org/users/login"
        - payload: {
            "user[login]": settings.AO3_USERNAME,
            "user[password]": settings.AO3_PASSWORD,
            "authenticity_token": "sample"
        }

    Potential pitfalls:
    - Will a mocked request work if it's not REST? And doesn't use JSON?
    """
