# Generated by Django 4.2.6 on 2023-11-04 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0003_alter_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='updateddate',
            field=models.DateField(auto_now=True),
        ),
    ]
