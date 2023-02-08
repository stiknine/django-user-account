from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import AccountCreateForm, AccountChangeForm
from .models import Account


class AccountAdmin(UserAdmin):
    """Custom user account admin."""
    add_form = AccountCreateForm
    form = AccountChangeForm
    model = Account
    list_display = ['username', 'email', 'full_name', 'last_login', 'is_staff', 'is_superuser']

    def full_name(self, obj):
        """Return user account full name for use in list_display."""
        return obj.get_full_name()


admin.site.register(Account, AccountAdmin)
