from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
    email = models.EmailField(max_length=250, null=False, blank=False)

    REQUIRED_FIELDS = [email]

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    twitter = models.CharField(max_length=50, null=True, blank=True, unique=True)
    telegram = models.CharField(max_length=50, null=True, blank=True, unique=True)
    instagram = models.CharField(max_length=50, null=True, blank=True, unique=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance=None, created=False, **kwargs):
    if created:
        Profile.objects.create(user=instance)
