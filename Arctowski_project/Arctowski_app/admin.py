from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import *

class MyAdminSite(AdminSite):
    login_template = 'login.html'
    site_header = "Polska Stacja Antarktyczna - Administracja "
    index_template = "main.html"
    app_index_template = "main.html"

class MyUserAdmin(admin.ModelAdmin):
    list_display = ('username','is_superuser','first_name','last_name','date_joined')

class CaseAdmin(admin.ModelAdmin):
    list_display = ('case_id','owner_name','owner_id')

class InCaseAdmin(admin.ModelAdmin):
    list_display = ('name','case_id')

class RaportAdmin(admin.ModelAdmin):
    list_display = ('rok','miesiac')
    list_filter = ('rok','miesiac')

class SekcjaAdmin(admin.ModelAdmin):
    list_display = ('tytul','raport_id')


class WpisAdmin(admin.ModelAdmin):
    list_display = ('tytul','sekcja_id')




admin.site.register(MyUser,MyUserAdmin)
admin.site.register(Case,CaseAdmin)
admin.site.register(InCase,InCaseAdmin)
admin.site.register(Raport,RaportAdmin)
admin.site.register(Sekcja,SekcjaAdmin)
admin.site.register(Wpis,WpisAdmin)
admin_site = MyAdminSite(name='myadmin')

