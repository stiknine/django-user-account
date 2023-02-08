from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Account


class AccountCreateForm(UserCreationForm):

    class Meta:
        model = Account
        fields = ("username", "email")


class AccountChangeForm(UserChangeForm):

    class Meta:
        model = Account
        fields = ("username", "email")
