from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    """Custom user account model.

    A subclass of Django's AbstractUser class. It overrides one method.
    A custom User model is the recommended way if using Django's user authentication system.
    """

    def __str__(self):
        return self.username
