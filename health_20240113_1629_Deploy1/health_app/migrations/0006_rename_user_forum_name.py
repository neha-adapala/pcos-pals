# Generated by Django 5.0.1 on 2024-01-02 21:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('health_app', '0005_remove_forum_name_forum_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='forum',
            old_name='user',
            new_name='name',
        ),
    ]