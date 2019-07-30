from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import FormView, CreateView
from .forms import RegistrationForm


class RegistrationView(FormView):
    form_class = RegistrationForm
    template_name = 'registration.html'
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = 'login.html'
    def form_valid(self, form):
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]

        user = authenticate(username=username, password=password)
        login(self.request, user)
        return super().form_valid(form)


