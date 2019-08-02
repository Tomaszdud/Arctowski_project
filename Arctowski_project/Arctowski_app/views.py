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
    template_name = 'create_case.html'
    success_url = '/case/add/things'

    def get_initial(self):
        initial = super(CreateCaseView, self).get_initial()
        if self.request.user.is_authenticated:
            user = self.request.user
            initial.update({'owner_name': user.username,
                            'owner':user.id})
        return initial

    def form_valid(self, form):
        case = form.save()
        length = form.cleaned_data['length']
        width = form.cleaned_data['width']
        height = form.cleaned_data['height']
        case.capacity = length*width*height
        return super().form_valid(form)


class CreateInCaseView(CreateView):
    model = InCase
    form_class = CreateInCaseForm
    template_name = 'create_case_things.html'
    success_url = '/case/add/things'

    def form_valid(self, form):
        incase = form.save()
        sum_of_val_thing = incase.value*incase.amount
        incase.case.sum_of_value += sum_of_val_thing
        incase.case.save()
        return super().form_valid(form)


class EndCaseView(RedirectView):
    url = '/miejscedodruku/'

    def get(self, request, *args, **kwargs):

        return super(EndCaseView, self).get(request, *args, **kwargs)