
def compruebaConvexo(param1):
    """DADA UNA MATRIZ DE ADYACENCIA, SE COMPRUEBA SI EL GRAFO ES CONEXO O NO.
    PARAMETROS: MATRIZ DE ADYACENCIA DEL GRAFO
    SALIDA: STRING ->  ES CONEXO||NO ES CONEXO"""

    encontrado = False
    verticesPendientes = []
    activo = 0
    verticesPendientes.append(activo)
    verticesPendientes = verticesPendientes + [-1]
    while verticesPendientes[activo] != -1:
        for k in range(activo, numVertices, 1):
            if param1[verticesPendientes[activo]][k] == 1 and not (existeVerticePendiente(verticesPendientes, k)):
                verticesPendientes.remove(-1)
                verticesPendientes.append(k)
                verticesPendientes.append(-1)
        activo += 1

    if verticesPendientes.__len__() == matrizAdy.__len__() + 1:
        #valorDevuelto = 1
        return "es conexo"
    else:
        #valorDevuelto = 0
        return "no es conexo"


def existeVerticePendiente(param1,param2):
    """COMPRUEBA SI EXISTE UN ELEMENTO EN UNA LISTA
    PARAMETROS: LISTA EN LA QUE SE REALIZA LA BUSQUEDA.
                ELEMENTO A BUSCAR EN LA LISTA
    SALIDA: BOOLEANO QUE INDICA SI EXISTE EL ELEMENTO"""

    existe=False
    if param1.__contains__(param2):
        existe=True
    return existe



"""COMIENZA LA EJECUCION"""

try:
    fInput = open("origen.txt","r")
    fOutput = open ("salida.txt","w")
except:
    print "Error al abrir fichero. Fin de la ejecucion"
    exit()

casos = int(fInput.readline())
for i in range(casos):
    numVertices = int(fInput.readline())
    numAristas = int(fInput.readline())
    matrizAdy = []
    for k in range(numVertices):
        matrizAdy.append([0] * numVertices)
    for j in range(numAristas):
        filas = int(fInput.readline())
        columnas = int(fInput.readline())
        matrizAdy[filas - 1][columnas - 1] = 1
        matrizAdy[columnas - 1][filas - 1] = 1
    resultado = []
    resultado="El grafo "
    resultado+=`i`
    resultado+=" " + compruebaConvexo(matrizAdy)
    resultado+="\n"
    fOutput.writelines(resultado)
