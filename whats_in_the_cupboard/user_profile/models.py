from django.db import models
from django.contrib.auth.models import User
# from rest_framework.authtoken.models import Token
# from django.dispatch import receiver


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='profile')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        """returns string representation to user"""
        return self.user.username

    @classmethod
    def active(cls):
        """Return all active profile instances"""
        return cls.objects.filter(is_active=True)

# @receiver(models.signals.post_save, sender=User)
# def create_profile(sender, **kwargs):
#     if kwargs['created']:
#         Token.objects.create(user=kwargs['instance'])
#         profile = ImagerProfile(user=kwargs['instance'])
#         profile.save()
