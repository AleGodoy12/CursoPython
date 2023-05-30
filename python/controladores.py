#Controladores de Flujo
#if (si)
#elif (si no, si)
#else (si no)

#IF
# edad = 30
# if edad >= 18:
#     print("Es un adulto")
    
# a = 25
# b = 50
# if b > a:
#  print("b es mas grande que a")

#Ejemplo de if con AND
# a = 195
# b = 30
# c = 400
# if a > b and c > a:
    #print("Ambas condiciones son verdaderas")

#Ejemplo de if con OR:

# a = 195
# b = 50
# c = 400
# if a > b or a > c:
#     print("Al menos una de las condiciones es verdadera")
    
# #Ejemplo con NOT:
# x = 10
# if not x > 15:
#     print("False")

#Else

# numeros = 24
# if numeros > 36:
#     print("El numero es mas grande")
# else:
#     print("El numero es mas chico")    

#Multiple if

# x = 25
# if x > 10:
#     print("Por encima de diez")
#     if x > 20:
#         print("Y tambien por encima de 20")
#     else:
#         print("Pero no por encima de 20")

#Elif
# a = 2 + 3
# if a == 4: 
#    print ("A es igual a cuatro")
# elif a == 5:
#    print ("A es igual a cinco")
# elif a == 6:
#    print ("A es igual a seis")
# else:
#    print ("No se cumple la condición")




#Controladores de flujo

#Iterar

#While - mientras
#Evalua la condicion 
#Si la condicion es False, se sale de la sentencia while y continua la ejecucion con la siguiente sentencia.
#Si la condicion es True, ejecuta cada una de las sentencias en el bloque y regresa al paso 1.


# num = 5
# while num > 0:
#     print(num)
#     num -=1
#     print("termino el conteo")
    
# n = 0
# while n <= 5:
#     n +=1
#     print("n vale", n)
# while True:
#  print("Esto es un bucle infinito!!!!!")

#While - Else
 
# chance = 1
# while chance <= 3:
#     txt = input("Escribe SI: ")
#     if txt == "SI":
#         print("Ok, lo conseguiste en el intento", chance)
#         break
#     chance +=1
# else:
#     print("Has agotado tus tres intentos")
    

#Instrucciones

#Continue

# i = 0
# while i < 6:
#     i +=1
#     if i == 3:
#         continue
#     print(i)

#Pass

# n = 0
# while n < 10:
#     n += 1
#     if n == 2:
#         pass
#     print('n vale' , n)
# n = 0
# while n < 10:
#     n += 1
#     if n == 2:
#         pass
#         print('n vale' , n)

#For

# lista = [1,2,3,4,5]
# for valor in lista:
#     print('Soy un item de la lista y valgo', valor)


# lista = [0,1,2,3,4,5,6,7,8,9,10]
# for num in lista:
#     print('Soy un valor de la lista y valgo', num)
#     num *= 5
#     print('Soy un valor de la lista y ahora valgo', num)


# texto = 'Hola Mundo, estoy usando for en Python'
# for letra in texto:
#     print(letra)
# texto2 = ''
# for letra in texto:
#     texto2 = letra * 2
# print(texto2)

# #Range
# range(0,1000)