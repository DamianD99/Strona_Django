from django.db import models

class Customer(models.Model):
    imie = models.CharField(max_length=200, null=True)
    nazwisko = models.CharField(max_length=200, null=True)
    content = models.TextField(blank=True, help_text='Opis klijęta')
    emial = models.CharField(max_length=200, null=True)
    telefon = models.CharField(max_length=200, null=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.imie

class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Produkty(models.Model):
    CATEGORY = (
        ('Drzwi', 'Drzwi'),
        ('Out Door', 'Out Door'),
    )

    name = models.CharField(max_length=200, null=True)
    kategoria = models.CharField(max_length=200, null=True)
    content = models.TextField(blank=True, help_text='Opis produktu')
    cena = models.FloatField(null=True)
    data = models.DateTimeField(auto_now_add=True, null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS = (
        ('Pakowane', 'Pakowane'),
        ('W drrodze do odbioercy', 'W drrodze do odbioercy'),
        ('Dostarczone', 'Dostarczone'),
    )

    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Produkty, null=True, on_delete=models.SET_NULL)
    cena = models.FloatField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
# Create your models here.
