from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.validators import MinLengthValidator
from django.utils.translation import gettext_lazy

from .models import Account


username_helptext = gettext_lazy('4 to 150 characters. Letters, numbers and @ . + - _ only.')
minlength_validator = MinLengthValidator(4, gettext_lazy('Enter a valid username, must be a minimum of 4 characters.'))


class AccountCreateForm(UserCreationForm):
    """User account creation form.

    A subclass of Django's UserCreationForm, which implements a custom user model.
    It updates the username field help_text and adds a min length validator.
    """

    class Meta:
        model = Account
        fields = ("username", "email")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = username_helptext
        self.fields['username'].validators = [minlength_validator]


class AccountChangeForm(UserChangeForm):
    """User account change form.

    A subclass of Django's UserChangeForm, which implements a custom user model.
    It updates the username field help_text and adds a min length validator.
    """

    class Meta:
        model = Account
        fields = ("username", "email")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = username_helptext
        self.fields['username'].validators = [minlength_validator]
