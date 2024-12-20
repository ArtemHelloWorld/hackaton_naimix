# Generated by Django 4.2.9 on 2024-11-16 15:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_remove_user_identity_confirmed"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="image",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="profile_image/%Y/%m/%d",
                verbose_name="аватарка",
            ),
        ),
    ]
