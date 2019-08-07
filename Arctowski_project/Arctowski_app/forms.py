from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Case, InCase, MyUser, Photo


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


class CaseEditForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = ['type','length','height','width','weight','storage_conditions','capacity']
        widgets = {'capacity':forms.HiddenInput}


class AddPhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = '__all__'
        widgets = {'photo_case':forms.HiddenInput}
