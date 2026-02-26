from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    profile_img = models.ImageField(
        null=True, blank=True, upload_to='profile_imgs/')
    age = models.IntegerField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True, default=None)

    # class Meta:
    #     constraints = [
    #         models.UniqueConstraint(
    #             fields=['email'],
    #             condition=models.Q(email__isnull=False) & ~models.Q(email=''),
    #             name='unique email'
    #         )
    #     ]

    def __str__(self) -> str:
        return self.username
