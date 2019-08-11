from django.contrib.auth import authenticate, login, logout, password_validation
from django.contrib.auth.forms import AuthenticationForm, SetPasswordForm
from jedi.evaluate.context import instance
from .forms import RegistrationForm,CreateCaseForm, CreateInCaseForm, ResetPass, CaseEditForm, AddPhotoForm
from .models import Case,InCase, MyUser, Photo
from django.contrib.auth.hashers import make_password
from django.utils.translation import gettext, gettext_lazy as _
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import (FormView, CreateView, RedirectView, View, DetailView, ListView, UpdateView, TemplateView)




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


class CaseListView(ListView):
    template_name = 'case_list.html'
    def get_queryset(self):
        queryset = Case.objects.filter(owner=self.request.user.id)
        return queryset

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


class EndCasePhoto(CreateView):
    model = Photo
    form_class = AddPhotoForm
    template_name = 'case_end.html'

    def get_success_url(self):
        return reverse_lazy('end_case', kwargs = {'pk':self.kwargs['pk']})

    def get_initial(self):
        initial = super(EndCasePhoto, self).get_initial()
        case = Case.objects.filter(owner=self.request.user.id).order_by('-pk')[0]
        initial.update({'photo_case':case.id})
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = Case.objects.filter(owner=self.request.user.id).order_by('-pk')[0]
        context['case'] = obj
        return context

    def form_valid(self, form):
        if form.cleaned_data['image'] is None and form.cleaned_data['scan'] is None:
            return redirect(self.get_success_url())
        else:
            print('lala')
            form.save()
        return super(EndCasePhoto,self).form_valid(form)

class EndCaseView(View):

    def post(self,request):
        for k,y in request.POST.items():
            if k == 'csrfmiddlewaretoken':
                continue
            else:
                if request.POST[k] is '':
                    case1 = Case.objects.filter(owner=self.request.user.id).order_by('-pk')[0]
                    ctx = {"case": case1}
                    return redirect('end_case', pk=case1.pk)
                else:
                    form = CreateInCaseForm(request.POST)
                    form.save()
                    case = Case.objects.get(pk=request.POST['case'])
                    case.sum_of_value = int(request.POST['value'])*int(request.POST['amount'])
                    case.save()
                    ctx = {"case": case}
                    return redirect('end_case', pk=case.pk)


class CaseEditView(UpdateView):
    template_name = 'case_edit.html'
    form_class = CaseEditForm
    model = Case
    success_url = '/case/list'

    def get_initial(self):
        initial = super(CaseEditView, self).get_initial()
        initial['capacity'] = 0.00
        return initial

    def form_valid(self, form):
        case = form.save()
        length = form.cleaned_data['length']
        width = form.cleaned_data['width']
        height = form.cleaned_data['height']
        case.capacity = length*width*height/1000000
        return super(CaseEditView,self).form_valid(form)


def add_error(param, error):
    pass


class Reset(FormView):
    form_class = ResetPass
    template_name = 'reset_password.html'
    success_url = '/home'
    def form_valid(self, form):
        error_messages = {
            'password_mismatch': _("The two password fields didn't match."),
        }
        user = MyUser.objects.get(username=form.cleaned_data['username'])
        password1 = form.cleaned_data.get("password1")
        password2 = form.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise Exception(
                error_messages['password_mismatch']
            )


        user.password = make_password(form.cleaned_data['password1'])
        user.save()
        return super(Reset,self).form_valid(form)






