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
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from Arctowski_app.views import (RegistrationView, LoginView, LogoutView, CreateCaseView\
                                 , CreateInCaseView, EndCaseView,CaseListView, CaseEditView, EndCasePhoto)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registration/', RegistrationView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('case/add/', CreateCaseView.as_view()),
    path('case/add/things/', CreateInCaseView.as_view()),
    path('case/end', EndCaseView.as_view()),
    path('case/list', CaseListView.as_view()),
    path('case/edit/<int:pk>', CaseEditView.as_view(),name='case_edit'),
    path('case/end/<int:pk>', EndCasePhoto.as_view(), name='end_case'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
