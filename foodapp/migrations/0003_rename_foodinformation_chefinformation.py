# Generated by Django 4.2.3 on 2023-11-25 17:40

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("realestate", "__first__"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("foodapp", "0002_comment_it_good_comment_rate"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="FoodInformation",
            new_name="ChefInformation",
        ),
    ]
