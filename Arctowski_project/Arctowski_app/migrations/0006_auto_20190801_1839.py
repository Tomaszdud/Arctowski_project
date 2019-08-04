# Generated by Django 2.2.3 on 2019-08-01 18:39

from django.contrib.auth.hashers import make_password
from django.db import migrations

def about_user(apps, schema_editor):
    MyUser = apps.get_model('Arctowski_app', 'MyUser')

    MyUser.objects.create(
        id="1",
        password='pbkdf2_sha256$150000$F3ltTNxwOma1$Giy3M84wv+f7veQOVbHswahwYDEF867+UqzlDjdo8x0=',
        is_superuser=False,
        username="JanKowalski1",
        first_name="Jan",
        last_name="Kowalski",
        email="jankowalski@gmail.com",
        is_staff=False,
        is_active=True,

    )

    MyUser.objects.create(
        id="2",
        password="pbkdf2_sha256$150000$ezPAG5nAOG49$ZoawKd4rnLIkEDJwpiGr5AWqXxnTN5ysrGpfGNx6vck=",
        is_superuser=False,
        username="AnnaNowak1",
        first_name="Anna",
        last_name="Nowak",
        email="annanowak@gmail.com",
        is_staff=False,
        is_active=True,

    )

    MyUser.objects.create(
        id="3",
        password="pbkdf2_sha256$150000$AHtBrdagDao7$8W0O5Y9kCEBtaqw53AYIDTnxzFSKnvqTfddk9WMoLRY=",
        is_superuser=True,
        username="admin",
        first_name="admin",
        last_name="admin",
        email="admin@gmail.com",
        is_staff=True,
        is_active=True,

    )

def about_case(apps, schema_editor):
    Case = apps.get_model('Arctowski_app', 'Case')
    MyUser = apps.get_model('Arctowski_app', 'MyUser')

    Case.objects.create(
        case_id="JK-SK-1",
        owner=MyUser.objects.get(pk=1),
        owner_name="Jan Kowalski",
        type="Skrzynia aluminiowa",
        length="80",
        width="60",
        height="60",
        weight="25",
        storage_conditions="ładownia",
        capacity="0.288",
        sum_of_value="6.800"
    )

    Case.objects.create(
        case_id="AN-SK-2",
        owner=MyUser.objects.get(pk=2),
        owner_name="Anna Nowak",
        type="Skrzynia aluminiowa",
        length="90",
        width="50",
        height="50",
        weight="30",
        storage_conditions="kabina",
        capacity="0.225",
        sum_of_value="5.000"
    )
def in_case(apps, schema_editor):
    InCase = apps.get_model('Arctowski_app', 'InCase')
    Case = apps.get_model('Arctowski_app', 'Case')

    InCase.objects.create(

        name="Ubrania",
        amount="1.0",
        unit_of_measurement="komplet",
        value="800",
        case=Case.objects.get(pk=1)
        )

    InCase.objects.create(
        name="Buty",
        amount="3.0",
        unit_of_measurement="para",
        value="300",
        case=Case.objects.get(pk=1)
        )

    InCase.objects.create(
        name="Elektornika osobista",
        amount="1.0",
        unit_of_measurement="komplet",
        value="1200",
        case=Case.objects.get(pk=1)
        )

    InCase.objects.create(
        name="Laptop DELL-numer seryjny ABC123456",
        amount="1.0",
        unit_of_measurement="sztuka",
        value="4500",
        case=Case.objects.get(pk=1)
        )


    InCase.objects.create(
        name="Ubrania",
        amount="1.0",
        unit_of_measurement="komplet",
        value="1000",
        case=Case.objects.get(pk=2)
        )

    InCase.objects.create(
        name="Książki",
        amount="3.0",
        unit_of_measurement="sztuka",
        value="200",
        case=Case.objects.get(pk=2)
        )

    InCase.objects.create(
        name="Elektornika osobista",
        amount="2.0",
        unit_of_measurement="komplet",
        value="2000",
        case=Case.objects.get(pk=2)
        )

    InCase.objects.create(
        name="Laptop Lenovo-numer seryjny ABC123489",
        amount="1.0",
        unit_of_measurement="sztuka",
        value="1800",
        case=Case.objects.get(pk=2)
        )

def date(apps, schema_editor):
    Raport = apps.get_model('Arctowski_app', 'Raport')

    Raport.objects.create(
        rok="2019",
        miesiac="styczeń"
        )

    Raport.objects.create(
        rok="2019",
        miesiac="luty"
        )

def in_section(apps, schema_editor):
    Sekcja = apps.get_model('Arctowski_app', 'Sekcja')
    Raport = apps.get_model('Arctowski_app', 'Raport')

    Sekcja.objects.create(
        tytul="Sprawozdanie techniczne",
        tekst_poczatek = "nie wiem co tu",
        tekst_koniec = "nie wiem co tu",
        raport = Raport.objects.get(pk=1)
        )

    Sekcja.objects.create(
        tytul="Park maszynowy",
        tekst_poczatek = "nie wiem co tu",
        tekst_koniec = "nie wiem co tu",
        sekcjaNadzedna = Sekcja.objects.get(tytul="Sprawozdanie techniczne"),
        raport = Raport.objects.get(pk=1)
        )

def create_wpis(apps, schema_editor):
    Wpis = apps.get_model('Arctowski_app','Wpis')
    Sekcja = apps.get_model('Arctowski_app', 'Sekcja')

    Wpis.objects.create(
    tytul = "Naprawa koparki",
    sekcja = Sekcja.objects.get(tytul="Park maszynowy")
    )


class Migration(migrations.Migration):

    dependencies = [
        ('Arctowski_app', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(about_user),
        migrations.RunPython(about_case),
        migrations.RunPython(in_case),
        migrations.RunPython(date),
        migrations.RunPython(in_section),
        migrations.RunPython(create_wpis),


    ]

