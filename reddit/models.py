from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Delete not use field
    username = None
    last_login = None
    is_staff = None
    is_superuser = None

    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    avatar = models.URLField(default="https://firebasestorage.googleapis.com/v0/b/valorantreddit-bc761.appspot.com/o/user_avatar%2Fdefault_avatar.png?alt=media&token=3796a9f0-32f7-48c0-b6d4-fb4e71455fd6")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email