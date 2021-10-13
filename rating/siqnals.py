from django.db.models.signals import post_save , post_delete
from django.dispatch import receiver
from django.core.cache import cache
from .models import Rating


@receiver(post_save, sender=Rating)
def create_profile(sender,  **kwargs):
    cache.clear()


@receiver(post_delete, sender=Rating)
def create_profile(sender,  **kwargs):
    cache.clear()