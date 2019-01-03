from django.db import models
from django.contrib.auth.models import User
from django.core.validators import email_re
from django.core.exceptions import ValidationError

# from rest_framework.authtoken.models import Token
# from django.dispatch import receiver


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='profile')
    email = models.EmailField(max_length=70, blank=True, unique=True)
    name = models.CharField(max_length=25, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        """returns string representation to user"""
        return self.user.username

    def save(self, *args, **kwargs):
        self.email = self.email.lower().strip()  # Hopefully reduces junk to ""
        if self.email != "":  # If it's not blank
            if not email_re.match(self.email):  # If it's not an email address
                raise ValidationError(
                    u'%s is not a valid email address' % self.email)
        if self.email == "":
            self.email = None
        super(UserProfile, self).save(*args, **kwargs)

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
