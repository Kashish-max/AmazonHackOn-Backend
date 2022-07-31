from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    profile_image = models.ImageField(
        upload_to="profile-images/",
        blank=True,
        null=True,
    )
    username = models.CharField(max_length=128, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    description = models.CharField(max_length=500, null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    private = models.BooleanField(default=False)
    
    def save(self, *args, **kwargs):
        if self.email == "":
            self.email = None
        super(User, self).save(*args, **kwargs)
    def delete_profile_image(self, using=None, keep_parents=False, *args, **kwargs):
        if self.profile_image.storage.exists(self.profile_image.name):
            self.profile_image.storage.delete(self.profile_image.name)
            self.profile_image = None
            self.save()