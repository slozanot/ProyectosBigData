#CADENAS
#Suma, producto, Type, len, count, find, join, partition, replace, split,
var1=[]
var2=[]
var1 = "Hola"
var2= " Adios"
print var1+var2
print var1*3


#LISTAS
#Suma, producto, Type, len, ExtraerPartes, ModificarPartes, append, count, extend, index, insert, pop, remove, reverse, sort,

var3 = []
var3 = [2,2,True,'una lista',[],[1,2],11,90,'hola','buenos','dias']
print var3[1]
print var3[1:3]
print var3[1:8:2]
print var3[:2]
print var3[2:]
print var3[::3]
print var3
var3[4:]= [True]
print var3
var3.append(4)
print var3
print var3.count(2)
var4 = [11,90,'hola','buenos','dias',23]
var3.extend(var4)
print var3
print var3.index(4,3,8)
var3.insert(0,'Primero')
print var3
var3.pop(12)
print var3
var3.remove(2)
print var3
var4=[0,1,2,3,4,5,6,7]
print var4
print var4.reverse()
print var4.sort()