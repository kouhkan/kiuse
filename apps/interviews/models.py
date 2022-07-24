from django.contrib.auth import get_user_model
from django.db import models


class Tag(models.Model):
    title = models.CharField(max_length=60, null=False, blank=False)
    slug = models.SlugField(max_length=60, null=False, blank=False, unique=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return self.slug


class Interview(models.Model):
    user = models.OneToOneField(get_user_model(), related_name="interview", on_delete=models.CASCADE)
    title = models.CharField(max_length=150, null=False, blank=False)
    about = models.TextField(null=False)
    job = models.TextField(null=False)
    gadget = models.TextField(null=False)
    software = models.TextField(null=False)
    art = models.TextField(null=True)
    tag = models.ManyToManyField(Tag, related_name="interview")
    approve = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return self.user.username
