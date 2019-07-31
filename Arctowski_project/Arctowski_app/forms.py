from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Case, InCase


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2','first_name','last_name']


class CreateCaseForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = '__all__'


class CreateInCaseForm(forms.ModelForm):
    class Meta:
        model = InCase
        fields = '__all__'

