# Generated by Django 4.1 on 2022-10-23 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("works", "0002_rename_completed_work_last_updated_date_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="work",
            old_name="last_updated_date",
            new_name="date_published",
        ),
        migrations.RenameField(
            model_name="work",
            old_name="posted_date",
            new_name="date_updated",
        ),
    ]