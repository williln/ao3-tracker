from django.db import models
from django.utils.translation import gettext_lazy as _

from django_extensions.db.models import TimeStampedModel


class Author(TimeStampedModel):
    url = models.URLField(help_text="URL to the author")
    username = models.CharField(max_length=100, help_text="Author's username")

    def __str__(self):
        return self.username


class Work(TimeStampedModel):
    class Status(models.TextChoices):
        TBR = "TBR", _("To Be Read")
        CR = "CR", _("Reading")
        READ = "READ", _("Read")
        DNF = "DNF", _("Did Not Finish")

    url = models.URLField()
    platform_id = models.CharField(
        null=True,
        max_length=100,
        help_text="ID of the work on the platform (AO3, FFN, etc.)",
    )
    author = models.ForeignKey(
        "works.Author",
        related_name="works",
        on_delete=models.SET_NULL,
        null=True,
    )
    title = models.CharField(max_length=255)
    summary = models.TextField(null=True)
    complete = models.BooleanField(default=False)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.TBR)
    word_count = models.PositiveIntegerField(default=0)
    posted_date = models.DateTimeField(null=True)
    last_updated_date = models.DateTimeField(null=True)

    def __str__(self):
        return f"{self.title} by {self.author.username}"
