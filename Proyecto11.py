import urllib2
import time
import math

def obtenerDatos():
    ficheroSalida = operarFicheros("Escritura", "ficheroContaminacionBruto.txt")
    ficheroLog = operarFicheros("Escritura", "LogContaminacion.txt")
    try:
        url = 'http://datos.madrid.es/datosabiertos/MEDIOAMBIENTE/CALIDAD_DEL_AIRE/2016/10/datos201610.txt'
        response = urllib2.urlopen(url=url)
        the_page = response.read()
        ficheroSalida.writelines(the_page)
    except:
        ficheroLog.writelines(time.strftime("%H%M"))
        ficheroLog.writelines("Error al solicitar los datos")
    ficheroSalida.close()
    ficheroLog.close()

def filtrarDatos
def obtenerMedia(fichero):
    contador=0
    suma=0
    for line in fichero:
        contador+=1
        suma+=int(line)
    return suma/contador

def obtenerVarianza(fichero,media):
    sumatorio=0
    contador=0
    for line in fichero:
        sumatorio+=math.pow(int(line)-media,2)
        contador+=1
    return sumatorio/contador

def operarFicheros(operacion,fichero):
    try:
        if operacion == 'Lectura':
            file = open(fichero,"r")
        elif operacion == 'Sobreescritura':
            file = open(fichero,"w")
        elif operacion == 'Escritura':
            file = open(fichero,"a")
        return file
    except:
        print "Error al abrir fichero"
        exit()

obtenerDatos()
fInput=operarFicheros('Lectura','ficheroContaminacionBruto.txt')
fOutput=operarFicheros('Escritura','ficheroContaminacion.txt')
filtrarDatos(28079004,28079038,28079040,fInput,fOutput)


