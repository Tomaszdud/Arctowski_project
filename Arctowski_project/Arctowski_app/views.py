from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import FormView, CreateView, RedirectView
from .forms import RegistrationForm,CreateCaseForm, CreateInCaseForm
from .models import Case,InCase


class RegistrationView(FormView):
    form_class = RegistrationForm
    template_name = 'registration.html'
    success_url = '/login/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = 'login.html'
    success_url = '/home/'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        user = authenticate(username=username, password=password)
        login(self.request, user)
        return super().form_valid(form)


class LogoutView(RedirectView):
    url = '/login/'

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)


class CreateCaseView(CreateView):
    model = Case
    form_class = CreateCaseForm
    template_name = 'blabla.html'
    success_url = '/case/add/things/'


class CreateInCaseView(CreateView):
    model = InCase
    form_class = CreateInCaseForm
    template_name = 'blabla1.html'
    success_url = '/home/'

