def comprobarResultado(param1,param2):
    if minimales.__len__()==numVertices:
        return "no tiene dependencias ciclicas"
    else:
        return "tiene dependencias ciclicas"

def buscarMinimales(param1,param2):
    minimal = True
    nuevosMinimales = False
    for j in range(param1.__len__()):
        for k in range(param1.__len__()):
            if param1[k][j] == 1:
                minimal = False
        if minimal and j not in param2:
            param2.append(j)
            nuevosMinimales = True
    return nuevosMinimales

try:
    fInput = open("origen.txt","r")
    fOutput = open("salida2.txt","w")
except:
    print "Error al abrir fichero. Fin de la ejecucion"
    exit()

casos = int(fInput.readline())
for i in range(casos):
    minimales = []
    numVertices = int(fInput.readline())
    numAristas = int(fInput.readline())
    matrizAdy = []
    for k in range(numVertices):
        matrizAdy.append([0] * numVertices)
    for j in range(numAristas):
        filas = int(fInput.readline())
        columnas = int(fInput.readline())
        matrizAdy[filas - 1][columnas - 1] = 1
    nuevosMinimales=buscarMinimales(matrizAdy, minimales)
    while nuevosMinimales == True:
        for verticeMinimal in range(minimales.__len__()):
            for k in range(matrizAdy.__len__()):
                matrizAdy[verticeMinimal][k] = 0
        nuevosMinimales = buscarMinimales(matrizAdy,minimales)

    resultado = "El grafo "
    resultado += `i`
    resultado +=" "+comprobarResultado(minimales,numVertices)
    resultado +="\n"
    fOutput.writelines(resultado)