# Generated by Django 4.2.9 on 2024-11-15 20:32

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="identity_confirmed",
        ),
    ]
