#Errores y excepciones

#Errores de sintaxis - Escritura de las instrucciones
#Errores excepcionales.

#print("Hola"
#SyntaxError: unexpected EOF while parsing 
#EOF = Signnifica end of line, el error nos indica que esperaba que se cierre el parentesis

#pint("Hola")

#Errores semanticos

# lista = []
# if len(lista) > 0:
#      lista.pop()

# number = float(input("ingresa un numero"))
# suma = 4
# print(number + suma)

#Excepciones - Try - Except

# try:
#     n = float(input("Ingrese un numero"))
#     m = 4
#     print(f"---> {n}/{m} = {n/m}")
# except:
#     print("Algo salio mal")
    
#Else
# while (True):
#     try:
#         a = float(input("Ingrese un numero: "))
#         b = float(input("Ingrese otro numero: "))
#         print(a +b)
#     except:
#         print("Ha ocurrido un error. Tienes que introducir dos numeros.")
#     else:
#         print("La suma se ha realizado correctamente")
#         break #Importante romper la itaracion si todo ha ido bien.
    
#Finally

# while (True):
#     try:
#         a = float(input("Ingrese un numero: "))
#         b = float(input("Ingrese otro numero: "))
#         print(a+b)
#     except:
#         print("Ha ocurrido un error.")
#     else: 
#         print("La suma se ha realizado")
#         break
#     finally:
#         print("Fin del bucle") #Esto se ejecuta siempre

