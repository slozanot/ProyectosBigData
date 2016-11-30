import urllib
import urllib2
import json
import time

def guardarDatosObtenidos (diccionario,ficheroSalida,*args):
    for i in range(diccionario['arrives'].__len__()):
        fOutput.writelines(str("Tiempo llegada: "))
        fOutput.writelines(str(diccionario['arrives'][i]['busTimeLeft']))
        fOutput.writelines(str(" Identificador bus: "))
        fOutput.writelines(str(diccionario['arrives'][i]['busId']))
        fOutput.writelines("\t")
    ficheroSalida.writelines("\n")

def obtenerDatos(numeroParada,ficheroSalida,ficheroLog):
    try:
        url = 'https://openbus.emtmadrid.es:9443/emt-proxy-server/last/geo/GetArriveStop.php'
        values = {'idClient':'WEB.SERV.100291103@alumnos.uc3m.es','passKey':'19AB6C00-7606-49C7-93A2-57E2F75CD313','idStop':str(numeroParada)}
        data = urllib.urlencode(values)
        response = urllib2.urlopen(url=url,data=data)
        the_page = response.read()
        guardarDatosObtenidos(json.loads(the_page),ficheroSalida,'lineId','busId','destination','busTimeLeft')
    except:
        ficheroLog.writelines("Error al solicitar los datos")
        return
try:
    fOutput = open("Output.txt","w")
    fLog = open("Log.txt","w")
except:
    print "Error al abrir fichero"
    exit()

while (1):

    obtenerDatos(4281,fOutput,fLog)
    time.sleep(2)
