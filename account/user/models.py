from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    """Custom user account model."""

    def __str__(self):
        return self.username
