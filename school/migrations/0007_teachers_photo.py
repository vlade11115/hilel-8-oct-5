# Generated by Django 4.2.5 on 2023-10-09 17:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("school", "0006_teachers_phone"),
    ]

    operations = [
        migrations.AddField(
            model_name="teachers",
            name="photo",
            field=models.ImageField(null=True, upload_to="teachers_photos"),
        ),
    ]
