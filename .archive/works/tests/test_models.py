from ..models import Author, Work


def test_author_creation(db):
    Author.objects.create(url="www.example.com", username="example")


def test_author_str(author):
    assert str(author) == author.username


def test_work_creation(author):
    Work.objects.create(
        url="www.example.com",
        author=author,
        title="Example",
    )


def test_work_str(work):
    assert str(work) == f"{work.title} by {work.author.username}"
