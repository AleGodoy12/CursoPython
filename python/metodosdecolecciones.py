#Metodos de colecciones

#Cadenas

#Upper

cadena = "hola mundo"
#print(cadena.upper())

#Lower
#print(cadena.lower())

#capitalize
#print(cadena.capitalize())

#Title
#print(cadena.title())

#Count
Frase = "Hola mundo esta cadena tiene muchas e"
#print(Frase.count("e"))

#Find
#print(Frase.find("mundo"))

#Rfind
#print(Frase.rfind("muchas"))

#Split
#Cadena = "Hola Mundo"
#print(Cadena.split())

#Join
# print(",".join(Cadena))

#Strip
Cadena = "--------Hola Mundo-------"
#print(Cadena.strip("-"))

#Replace
palabra = "Hola mundo"
#print(palabra.replace("o", "O"))


#Lista

#clear
letras = ["a","b","c","d"]
letras.clear()
#print(letras)

#Extend
listas1 = [1,2,3,4]
lista2 = [5,6,7,8]
#listas1.extend(lista2)
#print(listas1)

#Insert
# lista = [1,2,3,4,5]
# print(lista)
# lista.insert(2,0)
# print(lista)

#Reverse
listas1.reverse()
#print(listas1)

#sort
orden = [5,-10,35,0,-65,100]
orden.sort()
#print(orden)

#Conjuntos o Sets

#Copy
# set1 = {1,2,3,4}
# set2 = set1.copy()
# print(set2)

#Isdisjoint
set1 = {1,2,3}
set2 = {3,4,5}
# print(set1.isdisjoint(set2))

#issubset
set3 = {-1,99}
set4 = {1,2,3,4,5}
# print(set3.issubset(set4))

#Issuperset
set5 = {1,2,3}
set6 = {1,2}
# print(set5.issuperset(set6))

#Union
set7 = {1,2,3}
set8 = {3,4,5}
# print(set7.union(set8))

#difference

set9 = {1,2,3}
set10 = {3,4,5}
# print(set9.difference(set10))

#intersection
set11 = {1,2,3}
set12 ={3,4,5}
# print(set11.intersection(set12))

#Diccionarios

#Get
colores = {"amarillo":"yellow", "azul":"blue", "verde":"green"}
#print(colores.get("amarillo", "no hay clave amarillo"))

#Keys
#print(colores.keys())

#values
#print(colores.values())

#Items
# print(colores.items())
for clave, valor in colores.items():
    print(clave, valor)