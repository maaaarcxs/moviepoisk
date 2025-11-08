from django.db.models.signals import post_save, pre_save, pre_delete, post_delete, m2m_changed
from django.dispatch import receiver

from .models import Movie, MonthlySubscription, User


@receiver(post_save, sender=User)
def subscription_create_signal(sender, instance: User, created, **kwargs):
    if created:
        subscription = MonthlySubscription.objects.create(user=instance)