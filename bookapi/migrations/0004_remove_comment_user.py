# Generated by Django 4.2.6 on 2023-11-06 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookapi', '0003_comment_user_alter_comment_book'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
    ]
