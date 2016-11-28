#Funcion que voltea la lista de numeros binarios que recibe:
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

#Funcion que mapea la lista binaria con la lista de 0 a n-1 para construir las diferentes combinaciones de valores entre 0 y n-1
    #param1: Lista binaria que sirve como objeto de mapeo.
    #return: No devuelve nada


def obtenerListaFinal(param1):
    ListaFinal = []
    for x in range(len(param1)):
        if param1[x] == 1:
            ListaFinal.append(x)
        x+=1
    print ListaFinal


#Funcion principal. Solicita los numeros n y k al usuario. Creamos la lista binaria con tantos 1 como indica k.
        # Comenzamos a permutar la lista binaria
        # Muestra cada combinacion encontrada y al final un mensaje indicando el total de combinaciones encontradas

n=int(input("Introduce el valor de n "))
k=int(input("Introduce el valor de k "))
nuevaPermutacion=True
listaBinaria = [0]*(n-k)+[1]*k
obtenerListaFinal(listaBinaria)
contador=1
while nuevaPermutacion:
    nuevaPermutacion=obtenerPermutaciones(listaBinaria)
    if nuevaPermutacion:
        obtenerListaFinal(listaBinaria)
        contador+=1
print "El numero total de combinaciones es: "+str(contador)