# Generated by Django 5.0.1 on 2024-01-04 20:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health_app', '0007_remove_forum_name_forum_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forum',
            name='user',
        ),
        migrations.AddField(
            model_name='forum',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
