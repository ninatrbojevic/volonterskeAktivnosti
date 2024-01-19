from django.db import models

class Volonter(models.Model):
    ime = models.CharField(max_length=255)
    prezime = models.CharField(max_length=255)
    kontakt_email = models.EmailField()
    kontakt_telefon = models.CharField(max_length=15, blank=True, null=True)
    vjestine = models.TextField(blank=True, null=True)
    interesi = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.ime} {self.prezime}"

class Događaj(models.Model):
    naziv = models.CharField(max_length=255)
    datum_i_vrijeme = models.DateTimeField()
    opis = models.TextField()
    volonteri = models.ManyToManyField(Volonter, related_name='dogadaji')

    def __str__(self):
        return self.naziv

class Projekt(models.Model):
    naziv = models.CharField(max_length=255)
    opis = models.TextField()
    organizator = models.ForeignKey(Volonter, on_delete=models.CASCADE, related_name='organizirani_projekti')
    volonteri = models.ManyToManyField(Volonter, related_name='projekti')

    def __str__(self):
        return self.naziv
