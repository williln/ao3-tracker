# Generated by Django 4.1 on 2022-10-19 22:41

import django.db.models.deletion
import django_extensions.db.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Author",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    django_extensions.db.fields.CreationDateTimeField(
                        auto_now_add=True, verbose_name="created"
                    ),
                ),
                (
                    "modified",
                    django_extensions.db.fields.ModificationDateTimeField(
                        auto_now=True, verbose_name="modified"
                    ),
                ),
                ("url", models.URLField()),
                ("username", models.CharField(max_length=100)),
            ],
            options={
                "get_latest_by": "modified",
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Work",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    django_extensions.db.fields.CreationDateTimeField(
                        auto_now_add=True, verbose_name="created"
                    ),
                ),
                (
                    "modified",
                    django_extensions.db.fields.ModificationDateTimeField(
                        auto_now=True, verbose_name="modified"
                    ),
                ),
                ("url", models.URLField()),
                ("title", models.CharField(max_length=255)),
                ("summary", models.TextField(null=True)),
                ("complete", models.BooleanField(default=False)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("TBR", "To Be Read"),
                            ("CR", "Reading"),
                            ("READ", "Read"),
                            ("DNF", "Did Not Finish"),
                        ],
                        default="TBR",
                        max_length=10,
                    ),
                ),
                ("word_count", models.PositiveIntegerField(default=0)),
                ("posted", models.DateTimeField(null=True)),
                ("last_updated", models.DateTimeField(null=True)),
                ("completed", models.DateTimeField(null=True)),
                (
                    "author",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="works",
                        to="works.author",
                    ),
                ),
            ],
            options={
                "get_latest_by": "modified",
                "abstract": False,
            },
        ),
    ]