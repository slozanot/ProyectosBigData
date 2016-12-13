import urllib
import urllib2
import json
import time
import math

def guardarDatosObtenidos (diccionario,ficheroSalida,ficheroLog):
    try:
        ficheroSalida.writelines(str(diccionario['arrives'][0]['busTimeLeft']))
        ficheroSalida.writelines("\t")
    except:
        ficheroLog.writelines(time.strftime("%H%M"))
        ficheroLog.writelines("Error al escribir los datos")
    try:
        ficheroSalida.writelines("\n")
    except:
        ficheroLog.writelines(time.strftime("%H%M"))
        ficheroLog.writelines("Error al escribir los datos")

def obtenerDatos(numeroParada):
    horaActual = time.strftime("%H%M%S")
    time.sleep(1)
    while (time.strftime("%H%M%S") != horaActual):
        while ((time.strftime("%H%M") >= "0715") and (time.strftime("%H%M") <= "2215")):
            ficheroSalida = operarFicheros("Escritura", "Output.txt")
            ficheroLog = operarFicheros("Escritura", "Log.txt")
            try:
                url = 'https://openbus.emtmadrid.es:9443/emt-proxy-server/last/geo/GetArriveStop.php'
                values = {'idClient':'WEB.SERV.100291103@alumnos.uc3m.es','passKey':'19AB6C00-7606-49C7-93A2-57E2F75CD313','idStop':str(numeroParada)}
                data = urllib.urlencode(values)
                response = urllib2.urlopen(url=url,data=data)
                the_page = response.read()
                guardarDatosObtenidos(json.loads(the_page),ficheroSalida,ficheroLog)
            except:
                ficheroLog.writelines(time.strftime("%H%M"))
                ficheroLog.writelines("Error al solicitar los datos")
            ficheroSalida.close()
            ficheroLog.close()
            time.sleep(300)
        time.sleep(32400)

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

obtenerDatos(4281)
fOutput = operarFicheros("Lectura","Output.txt")
media = obtenerMedia(fOutput)
print "Media obtenida: "+str(media)+ " segundos"
operarFicheros('Cierre',fOutput)
fOutput = operarFicheros('Lectura',"Output.txt")
fLog = operarFicheros('Escritura',"Log.txt")
varianza = obtenerVarianza(fOutput,media)
print "Varianza obtenida: "+str(varianza)

