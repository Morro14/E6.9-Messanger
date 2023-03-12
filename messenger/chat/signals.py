from django.dispatch import receiver
from django.db.models import signals
from .models import MyUser
from django.utils.text import slugify


@receiver(signals.pre_save, sender=MyUser)
def add_slug(sender, instance, **kwargs):
    instance.slug = slugify(instance.username)
    
    
    