from django.db.models.signals import pre_save
from django.dispatch import receiver

from school.models import Subject


@receiver(pre_save, sender=Subject)
def my_callback(sender, instance, **kwargs):
    if instance.name == "Math":
        instance.score = 2
    print(f"Model saved! Sender was {sender} kwargs {kwargs}")
