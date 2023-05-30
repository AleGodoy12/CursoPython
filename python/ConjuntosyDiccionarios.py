#Conjutos y diccionarios

#set
cojunto = {1,2,3,4}
otr_conjunto = {"hola", "mundo"}

# variable = {2,1,4,"mundo"}
# print(type(variable))

# set1 = set([1, 2, 3, 4])
# print(set1)
# set2 = set(range(10))
# print(set2)
# mi_lista=list({1, 2, 3, 4})
# mi_set = set(mi_lista)
# print(type(mi_set))

#Funciones de conjunto o set

#ADD

# numeros = {1,2,3,4}
# numeros.add(5*2)
# print(numeros)

#UPDATE
# numeros = {1,2,3,4}
# numeros.update([5,6,7,8])
# print(numeros)
# numeros.update(range(9,13))
# print(numeros)

#Len
numeros = {1,2,3,4}
#print(len(numeros))

#Discard
# numeros = {1,2,3,4}
# numeros.discard(5)
# print(numeros)

#Remove
# numeros = {1,2,3,4}
# numeros.remove(3)
# print(numeros)

#IN

# numeros = {1,2,3,4}
# print(5 in numeros)

#CLEAR

# numeros = {1,2,3,4}
# numeros.clear()
# print(numeros)

#POP
# numeros =  {1,2,3,4,5,6,7,8}
# while numeros:
#     print("Se está borrando: ", numeros.pop())



#Diccionarios
# colores = {"Amarillo":"Yellow", "Azul":"Blue", "Rojo": "Red"}
# colores ["Amarillo"] = "White"
# print(colores["Amarillo"])

#Asignacion
# edades = {"Juan":26, "Esteban": 35, "Maria": 29}
# edades["Juan"]+=5
# print(edades["Juan"])
# edades["Maria"]*=2
# print(edades["Maria"])

#Funciones de diccionarios

#ADD
# numeros = {"uno":1, "dos":2,"tres":3, "cuatro":4}
# numeros["cinco"]=5
# print(numeros)

#UPDATE
numeros = {"uno":1, "dos":2,"tres":3, "cuatro":4}
numeros.update({"cinco":5, "seis":6})
#print(numeros)

#DEL
numeros = {"uno":1, "dos":2,"tres":3, "cuatro":4}
del numeros["dos"]
#print(numeros)

#IN
numeros = {"uno":1, "dos":2,"tres":3, "cuatro":4}
#print("seis" in numeros)

#Clear
numeros = {"uno":1, "dos":2,"tres":3, "cuatro":4}
numeros.clear()
print(numeros)
