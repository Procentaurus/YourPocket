from django.db.models.signals import post_save
from django.contrib.auth.models import Group, User

from .models import Customer

def user_profile(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='customer')
        instance.groups.add(group)
        Customer.objects.create(
            user=instance,
            name=instance.username,
            email=instance.email,
        )
post_save.connect(user_profile,sender=User)
