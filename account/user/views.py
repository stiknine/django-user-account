from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import AccountCreateForm


class IndexView(generic.TemplateView):
    """Index page view."""

    template_name = 'index.html'


class HomeView(LoginRequiredMixin, generic.TemplateView):
    """Home page view."""

    login_url = reverse_lazy('login')
    template_name = 'home.html'


class RegisterView(generic.edit.CreateView):
    """User account registration view."""

    form_class = AccountCreateForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'
