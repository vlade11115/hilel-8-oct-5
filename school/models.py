from django.db import models


class Subject(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    score = models.PositiveIntegerField()

    def __str__(self):
        return f"ID: {self.pk} {self.name}"


class Teachers(models.Model):
    first_name = models.CharField(max_length=50)
    subjects = models.ManyToManyField(Subject, related_name="teachers")

    def __str__(self):
        return f"ID: {self.pk} {self.first_name}"


class Groups(models.Model):
    name = models.CharField(max_length=50)
    teacher = models.ForeignKey(Teachers, on_delete=models.PROTECT)
