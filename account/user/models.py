from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy


class Account(AbstractUser):
    """Custom user account model.

    A subclass of Django's AbstractUser class. It overrides one method and updates email to be a unique field.
    A custom User model is the recommended way if using Django's user authentication system.
    """

    email = models.EmailField(
        gettext_lazy("email address"),
        unique=True,
        error_messages={
            "unique": gettext_lazy("A user with that email already exists."),
        },
    )

    def __str__(self):
        return self.username
