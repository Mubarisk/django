# Generated by Django 3.2.5 on 2021-07-23 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_userprofile_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='like',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
