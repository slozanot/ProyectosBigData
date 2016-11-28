#Funcion que voltea la lista de numeros que recibe:
    #param1: Lista a voltear
    #param2: Indicar si solo se quiere voltear un trozo de la lista.
    #return: No devuelve nada

def reordenar(param1,param2=0):
    k=-1
    while(k>param2):
        aux=param1[k]
        param1[k]=param1[param2]
        param1[param2]=aux
        k-=1
        param2+=1


#Funcion que busca en la lista de derecha a izquierda el primer valor mayor que uno dado:
    #param1: Lista en la que se busca
    #param2: Valor a buscar el mayor.
    #return: Devuelve la posicion del valor encontrado

def buscarPosicionMayor(param1,param2):
    i = -1
    while param1[i]<=param2:
        i-=1
    return i

#Funcion que dada una lista, calcula la siguiente permutacion siguiendo un algoritmo
    #param1: Lista para permutar
    #return: Valor booleano que indica si se ha encontrado una nueva permutacion

def obtenerPermutaciones(param1):
    nuevaPermutacion = False
    i=-1
    while not nuevaPermutacion and abs(i) < len(param1):
        if param1[i-1]<param1[i]:
            aux = param1[i-1]
            indice=buscarPosicionMayor(param1[i-1:],aux)
            param1[i-1]=param1[indice]
            param1[indice] = aux
            reordenar(param1,i)
            nuevaPermutacion = True
        i-=1
    return nuevaPermutacion

#Funcion principal. Se crea la lista de numeros enteros
        # Comenzamos a permutar la lista
        # Muestra cada permutacion encontrada y al final un mensaje indicando el total de combinaciones encontradas

contador=0
Entero=[0,1,3,2]
nuevaPermutacion= True
print Entero
contador+=1
while nuevaPermutacion:
    nuevaPermutacion=obtenerPermutaciones(Entero)
    print Entero
    contador+=1
print "El numero de permutaciones totales es: "+str(contador)
