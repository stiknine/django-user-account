from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Account


class AccountCreateForm(UserCreationForm):
    """User account creation form.

    A subclass of Django's UserCreationForm, which implements the custom user model.
    """

    class Meta:
        model = Account
        fields = ("username", "email")


class AccountChangeForm(UserChangeForm):
    """User account change form.

    A subclass of Django's UserChangeForm, which implements the custom user model.
    """

    class Meta:
        model = Account
        fields = ("username", "email")
