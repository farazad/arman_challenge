# Generated by Django 5.0.1 on 2024-01-06 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ticket_volley", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="seat",
            name="is_reserved",
            field=models.BooleanField(default=False),
        ),
    ]
