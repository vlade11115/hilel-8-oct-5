# Generated by Django 4.2.5 on 2023-10-09 17:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("school", "0005_alter_teachers_subjects"),
    ]

    operations = [
        migrations.AddField(
            model_name="teachers",
            name="phone",
            field=models.CharField(max_length=30, null=True),
        ),
    ]