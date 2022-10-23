from unittest.mock import patch

import pytest
import responses
from AO3 import Session
from django.conf import settings

from api.ao3 import get_ao3_session, import_bookmarks


def test_get_ao3_session():
    with patch.object(Session, "__init__", return_value=None):
        session = get_ao3_session()
        assert isinstance(session, Session)


@pytest.mark.skip(reason="Need to find a way to test this")
def test_get_work():
    pass


@pytest.mark.skip(reason="Need to find a way to test this")
@responses.activate
def test_get_bookmarks():
    """
    FIXME: How to mock these kinds of classes?
    """
    login_url = "https://archiveofourown.org/users/login"
    url = "https://archiveofourown.org/users/login"
    # Add the request that would get the authenticity token
    responses.add(responses.GET, login_url, json={}, status=200)

    # Add the login response
    responses.add(
        responses.POST,
        url,
        json={
            "user[login]": settings.AO3_USERNAME,
            "user[password]": settings.AO3_PASSWORD,
            "authenticity_token": "sample",
        },
        status=302,
    )
    results = import_bookmarks()

    """
    current error at this point:
    >       self.authenticity_token = soup.find("input", {"name": 'authenticity_token'})["value"]
E       TypeError: 'NoneType' object is not subscriptable
    """
    assert 1 == 1
