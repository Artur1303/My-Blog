# Generated by Django 2.2.13 on 2020-10-08 13:32

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0016_like'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Like',
            new_name='ArticleLike',
        ),
    ]
