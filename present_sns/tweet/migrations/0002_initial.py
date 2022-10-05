# Generated by Django 4.1.1 on 2022-10-05 07:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("tweet", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="tweetmodel",
            name="username",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="comment",
            name="username",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="comment",
            name="write_no",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="tweet.tweetmodel"
            ),
        ),
    ]
