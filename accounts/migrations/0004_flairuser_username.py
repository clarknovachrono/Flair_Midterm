# Generated by Django 4.1.2 on 2022-10-24 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0003_remove_flairuser_username"),
    ]

    operations = [
        migrations.AddField(
            model_name="flairuser",
            name="username",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]