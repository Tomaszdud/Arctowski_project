from django.contrib.auth.forms import UserCreationForm, PasswordResetForm, SetPasswordForm, UsernameField
from django import forms
from .models import Case, InCase, MyUser, Photo
from django.contrib.auth import authenticate,password_validation,get_user_model
from django.utils.translation import gettext, gettext_lazy as _

UserModel = get_user_model()



class RegistrationForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ['username','password1','password2','first_name','last_name']



class CreateCaseForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = '__all__'
        exclude = ['sum_of_value']
        widgets = {'owner_name': forms.HiddenInput(),'owner': forms.HiddenInput(),'capacity':forms.HiddenInput()}


class CreateInCaseForm(forms.ModelForm):
    class Meta:
        model = InCase
        fields = '__all__'


class ResetPass(forms.Form):
    error_messages = {
        'password_mismatch': _("The two password fields didn't match."),
    }
    username = forms.CharField(max_length=50)

    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput,
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput,
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )


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


class IncaseEditForm(forms.ModelForm):
    class Meta:
        model = InCase
        fields = ['name','value','amount','unit_of_measurement']

