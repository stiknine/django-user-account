from django.views import generic
from django.urls import reverse_lazy

from .forms import AccountCreateForm


class IndexView(generic.TemplateView):
    """Index home page view."""

    template_name = 'index.html'


class RegisterView(generic.edit.CreateView):
    """User account registration view."""

    form_class = AccountCreateForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'
