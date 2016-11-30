import urllib
import urllib2
import json
import time

def guardarDatosObtenidos (diccionario,ficheroSalida,ficheroLog):
    for i in range(diccionario['arrives'].__len__()):
        try:
            ficheroSalida.writelines(str("Tiempo llegada: "))
            ficheroSalida.writelines(str(diccionario['arrives'][i]['busTimeLeft']))
            ficheroSalida.writelines(str(" Identificador bus: "))
            ficheroSalida.writelines(str(diccionario['arrives'][i]['busId']))
            ficheroSalida.writelines("\t")
        except:
            ficheroLog.writelines(time.strftime("%H%M"))
            ficheroLog.writelines("Error al escribir los datos")
    try:
        ficheroSalida.writelines("\n")
    except:
        ficheroLog.writelines(time.strftime("%H%M"))
        ficheroLog.writelines("Error al escribir los datos")

def obtenerDatos(numeroParada,ficheroSalida,ficheroLog):
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
        time.sleep(2)

while(1):
    while((time.strftime("%H%M")>="0715")and(time.strftime("%H%M")<="2215")):
        try:
            fOutput = open("Output.txt", "a")
            fLog = open("Log.txt", "a")
        except:
            print "Error al abrir fichero"
            exit()
        obtenerDatos(4281,fOutput,fLog)
        time.sleep(300)
        fOutput.close()
        fLog.close()
    time.sleep(32400)
