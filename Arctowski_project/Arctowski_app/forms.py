from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Case, InCase, MyUser


class RegistrationForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ['username','password1','password2','first_name','last_name']


class CreateCaseForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = '__all__'
        exclude = ['capacity','sum_of_value']
        widgets = {'owner_name': forms.HiddenInput(),'owner': forms.HiddenInput()}


class CreateInCaseForm(forms.ModelForm):
    class Meta:
        model = InCase
        fields = '__all__'

