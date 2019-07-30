from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import FormView, CreateView
from .forms import RegistrationForm


class RegistrationView(FormView):
    form_class = RegistrationForm
    template_name = 'registration.html'
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)