# Generated by Django 4.0.5 on 2022-06-10 05:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gram', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reel', models.FileField(upload_to='reel')),
                ('likes', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('story', models.ImageField(upload_to='story')),
            ],
        ),
        migrations.RemoveField(
            model_name='follow',
            name='followed',
        ),
        migrations.RemoveField(
            model_name='follow',
            name='follower',
        ),
        migrations.AlterModelOptions(
            name='post',
            options={},
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='author',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='post',
            name='dislikes',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='location',
        ),
        migrations.AddField(
            model_name='profile',
            name='followers',
            field=models.ManyToManyField(blank=True, related_name='followers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='profile',
            name='followings',
            field=models.ManyToManyField(blank=True, related_name='followings', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(upload_to='profilepics'),
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Follow',
        ),
        migrations.AddField(
            model_name='story',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gram.profile'),
        ),
    ]
