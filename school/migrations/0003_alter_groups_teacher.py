# Generated by Django 4.2.5 on 2023-10-05 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("school", "0002_teachers_groups"),
    ]

    operations = [
        migrations.AlterField(
            model_name="groups",
            name="teacher",
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to="school.teachers"),
        ),
    ]
