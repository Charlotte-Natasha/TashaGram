# Generated by Django 4.0.5 on 2022-06-10 05:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gram', '0003_reels_story_remove_follow_followed_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user',
            new_name='author',
        ),
    ]
