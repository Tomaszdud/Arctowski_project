from django.db import models
from django.contrib.auth.models import User

STORAGE = (())


class Case(models.Model):
    case_id = models.CharField(max_length=20)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
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
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=12, decimal_places=1)
    unit_of_measurement = models.CharField(max_length=50)
    value = models.DecimalField(max_digits=11, decimal_places=2)
    case = models.ForeignKey(Case, on_delete=models.CASCADE)


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

