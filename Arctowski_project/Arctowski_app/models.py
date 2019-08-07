from django.db import models
from django.contrib.auth.models import AbstractUser


STORAGE = (('pokład','pokład'),
           ('ładownia','ładownia'),
            ('kabina','kabina'),
            ('+4','+4'),
            ('-20','-20'),
            ('-80','-80'),
           )


class MyUser(AbstractUser):
    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'


class Case(models.Model):
    case_id = models.CharField(max_length=20)
    owner = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    owner_name = models.CharField(max_length=60)
    type = models.CharField(max_length=50)
    length = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()
    weight = models.DecimalField(max_digits=11, decimal_places=1)
    storage_conditions = models.CharField(max_length = 20, choices=STORAGE)
    capacity = models.DecimalField(max_digits=12, decimal_places=2, null=True)
    sum_of_value = models.DecimalField(max_digits=13, decimal_places=2, default=0.00)

    def __str__(self):
        return self.case_id


class InCase(models.Model):
    name = models.CharField(max_length=100,null=True, blank=True)
    amount = models.DecimalField(max_digits=12, decimal_places=1, null=True,blank=True)
    unit_of_measurement = models.CharField(max_length=50,null=True, blank=True)
    value = models.DecimalField(max_digits=11, decimal_places=2, null=True, blank=True)
    case = models.ForeignKey(Case, on_delete=models.CASCADE, null=True, blank=True)


class Raport(models.Model):
    rok = models.CharField(max_length=30)
    miesiac = models.CharField(max_length=30)

    def get_as_html(self):
        buffer = '''<h1>Raport za {} {}</h1>'''.format(self.rok, self.miesiac)

        for sekcja in self.sekcje.filter(sekcjaNadzedna=None):
            buffer += sekcja.get_as_html(1)
        return buffer


class Sekcja(models.Model):
    tytul = models.CharField(max_length=128)
    tekst_poczatek = models.CharField(max_length=128, blank=True, null=True)
    tekst_koniec = models.CharField(max_length=128,  blank=True, null=True)
    sekcjaNadzedna = models.ForeignKey('self', related_name='podSekcje', on_delete=models.CASCADE, blank=True, null=True)
    raport = models.ForeignKey(Raport, related_name='sekcje', on_delete=models.CASCADE ,  blank=True, null=True)

    def get_as_html(self,level=1):
        buffer = '''<h{}>{}</h{}>
        <div class="opis_wstep level_{}">{}</div>'''.format(level,self.tytul,level,level,self.tekst_poczatek)

        for podSekcja in self.podSekcje.all():

            buffer += podSekcja.get_as_html(level+1)

        return buffer + '<div class="opis_koniec level_{}">{}</div>'.format(level,self.tekst_koniec)


class Wpis(models.Model):
    tytul = models.CharField(max_length=128)
    sekcja = models.ForeignKey(Sekcja,related_name='wpisy', on_delete=models.CASCADE)


class Photo(models.Model):

    def group_based_upload_to(instance, filename):
        return "cases/{}/{}".format(instance.photo_case.case_id, filename)

    image = models.ImageField(upload_to=group_based_upload_to, null=True, blank=True)
    scan = models.FileField(upload_to=group_based_upload_to, null=True, blank=True)
    photo_case = models.ForeignKey(Case, on_delete=models.DO_NOTHING)