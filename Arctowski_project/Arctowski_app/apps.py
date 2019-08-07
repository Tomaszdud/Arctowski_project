from django.apps import AppConfig
from django.contrib.admin.apps import AdminConfig

class ArctowskiAppConfig(AppConfig):
    name = 'Arctowski_app'


class MyAdminConfig(AdminConfig):
    default_site = 'Arctowski_project.admin.MyAdminSite'