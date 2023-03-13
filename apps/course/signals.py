from django.db.models import Avg
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Certificate


@receiver(post_save, sender=Certificate)
def update_course_avg_rate(sender, instance, created, **kwargs):
    if created:
        instance.course.rate = instance.course.course_certificates.all().aggregate(Avg('rate'))['rate__avg']
        instance.course.save()
