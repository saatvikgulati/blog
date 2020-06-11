from django.db.models.signals import post_save #signal
from django.contrib.auth.models import User #sender
from django.dispatch import receiver #reciever
from .models import Profile #profile to work on

@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save,sender=User)
def save_profile(sender,instance,**kwargs):
    instance.profile.save()