"""Arctowski_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
#from Arctowski_app.admin import admin_site
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from Arctowski_app.views import (RegistrationView, LoginView, LogoutView, CreateCaseView\
                                 , CreateInCaseView, EndCaseView,CaseListView, CaseEditView, EndCasePhoto, Reset, HomeView\
                                 ,IncaseEditView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('registration/', RegistrationView.as_view()),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('case/add/', CreateCaseView.as_view(), name='case_add'),
    path('case/add/things/', CreateInCaseView.as_view()),
    path('case/end', EndCaseView.as_view()),
    path('admin/password_reset/',auth_views.PasswordResetView.as_view(),name='admin_password_reset'),
    path('admin/password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    path('reset/password', Reset.as_view()),
    path('case/', CaseListView.as_view(), name='case'),
    path('case/edit/<int:pk>', CaseEditView.as_view(),name='case_edit'),
    path('incase/edit/<int:pk>/', IncaseEditView.as_view(),name='incase_edit'),
    path('case/end/<int:pk>', EndCasePhoto.as_view(), name='end_case'),

    path('', HomeView.as_view(), name='home')

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
