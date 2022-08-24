from django.db import models

# Create your models here.
class Abuelos(models.Model):
    nombre= models.CharField(max_length=40)
    edad= models.IntegerField()
    fechaNacimiento= models.CharField(max_length=40)
    profesion= models.CharField(max_length=40)

class Padres(models.Model):
    nombre= models.CharField(max_length=40)
    edad= models.IntegerField()
    fechaNacimiento= models.CharField(max_length=40)
    profesion= models.CharField(max_length=40)

class Primos(models.Model):
    nombre= models.CharField(max_length=40)
    edad= models.IntegerField()
    fechaNacimiento= models.CharField(max_length=40)
    colorFavorito= models.CharField(max_length=40)
