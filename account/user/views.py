from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from .forms import AccountCreateForm


def index_view(request):
    return render(request, 'index.html')


class RegisterView(generic.edit.CreateView):
    form_class = AccountCreateForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'
