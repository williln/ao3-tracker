import pytest
from model_bakery import baker


@pytest.fixture
def author(db):
    return baker.make("works.Author")


@pytest.fixture
def work(db, author):
    return baker.make("works.Work", author=author)
