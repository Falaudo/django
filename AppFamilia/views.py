from django.http import HttpResponse
from django.shortcuts import render
from .models import Abuelos, Padres, Primos
from django.template import loader
# Create your views here.


def abuelos(request):
    dolly = Abuelos(nombre="Dolly", edad=87,
                    fechaNacimiento="3/8/1935", profesion="Profesora de Bordado")
    dolly.save()
    olga = Abuelos(nombre="Olga", edad=78, fechaNacimiento="7/12/1944",
                   profesion="Profesora de Historia y Geografía")
    olga.save()
    antonio = Abuelos(nombre="Antonio", edad=73,
                      fechaNacimiento="12/1/1949", profesion="Profesor de Mecánica")
    antonio.save()
    textoabus = f"<h1>Abuelos</h1>"
    textoDolly = f"<h1>nombre: { dolly.nombre }, edad:{ dolly.edad }, fecha de nacimiento: { dolly.fechaNacimiento }, profesión: { dolly.profesion }</h1>"
    textoOlga = f"<h1>nombre: { olga.nombre }, edad:{ olga.edad }, fecha de nacimiento: { olga.fechaNacimiento }, profesión: { olga.profesion }</h1>"
    textoAntonio = f"<h1>nombre: { antonio.nombre }, edad:{ antonio.edad }, fecha de nacimiento: { antonio.fechaNacimiento }, profesión: { antonio.profesion }</h1>"
    texto = textoabus, textoDolly, textoOlga, textoAntonio
    return HttpResponse(texto)

def padres(request):
    madre= Padres(nombre="Marcela", edad=53,
                    fechaNacimiento="27/10/1969", profesion="Arquitecta")
    madre.save()      
    padre=Padres(nombre="Sergio", edad=54,
                    fechaNacimiento="29/7/1968", profesion="Contador Público")    
    padre.save()              
    textopadres = f"<h1>Padres</h1>"
    textomadre = f"<h1>nombre: { madre.nombre }, edad:{ madre.edad }, fecha de nacimiento: { madre.fechaNacimiento }, profesión: { madre.profesion }</h1>"
    textopadre = f"<h1>nombre: { padre.nombre }, edad:{ padre.edad }, fecha de nacimiento: { padre.fechaNacimiento }, profesión: { padre.profesion }</h1>"     
    texto = textopadres, textomadre, textopadre
    return HttpResponse(texto) 

def primos(request):
    manu = Primos(nombre="Manuel", edad=9,
                    fechaNacimiento="3/5/2013", colorFavorito="Azul")
    manu.save()
    bruno = Primos(nombre="Bruno", edad=6, fechaNacimiento="27/1/2016",
                   colorFavorito="Verde")
    bruno.save()
    mateo= Primos(nombre="Mateo", edad=2,
                      fechaNacimiento="27/09/2019", colorFavorito="Amarillo")
    mateo.save()
    textoprim = f"<h1>Primos</h1>"
    textoManu = f"<h1>nombre: { manu.nombre }, edad:{ manu.edad }, fecha de nacimiento: { manu.fechaNacimiento }, color favorito: { manu.colorFavorito }</h1>"
    textoBruno = f"<h1>nombre: { bruno.nombre }, edad:{ bruno.edad }, fecha de nacimiento: { bruno.fechaNacimiento }, color favorito: { bruno.colorFavorito }</h1>"
    textoMateo = f"<h1>nombre: { mateo.nombre }, edad:{ mateo.edad }, fecha de nacimiento: { mateo.fechaNacimiento }, color favorito: { mateo.colorFavorito }</h1>"
    texto = textoprim, textoManu, textoBruno, textoMateo
    return HttpResponse(texto)  

def familiaApp(request):
    abuelos = '/abuelos'
    padres = '/padres'
    primos = '/primos'
    diccionario = {
        'abuelos': abuelos,
        'padres': padres,
        'primos': primos,
    }
    plantilla = loader.get_template('template1.html')
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)