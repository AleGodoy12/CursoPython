#Funciones
# len()

# def nombre(parametros):
#     sentencias
#     return(expresion)

# def saludar():
#     print("Estoy saludando desde una funcion")
# saludar()

# def saludando_con_nombre(nombre):
#     saludando = print("Hola {}! como estas?".format(nombre))
#     return saludando
# saludando_con_nombre("Juan")

variable_test = 10
# def test():
#     variable_test = 155
#     print(variable_test)
# test()

#retornando valores

# return
# def saludando_con_nombre(nombre):
#     saludando = print("Hola {}! como estas?".format(nombre))
#     return saludando
# saludando_con_nombre("Ale")

#NOTA: Por defecto, las funciones retornan el valor None.

#funciones con colecciones:

# def lista():
#     return[1,2,3,4,5]
# print(lista()[1:3])

# variable = lista()
# variable[1:4]

#Definir y llamar funciones con parametros

# def saludo(nombre):
#     print(f"Hola + {nombre}")

# def nombre_Edad(nombre,edad):
#     print(f"soy {nombre} y tengo {edad} años!")
    
# def saludo(nombre):
#     print(f"Hola {nombre}")
# saludo("Gabriel")
# saludo("Juan")
# saludo("Daniela")

# def saludo(nombre,apellido):
#     print(f"Hola, {nombre} {apellido}")
# saludo("Avila", "Juan")


# def lenguajefav(nombre, lenguaje):
#     print(f"hola, soy {nombre} y mi lenguaje favorito es {lenguaje}")
# lenguajefav(nombre="Ale", lenguaje="Python")
# def lenguajefav(nombre, lenguaje):
#     print(f"hola, soy {nombre} y mi lenguaje favorito es {lenguaje}")
# lenguajefav(lenguaje="Python", nombre="Ale")

# def lenguajefav(nombre, lenguaje):
#     print(f"hola, soy {nombre} y mi lenguaje favorito es {lenguaje}")
# lenguajefav("Ale", "Python")

# def fav_lenguaje(lenguaje="Python"):
#     print(f"Mi lenguaje favorito de programación es {lenguaje}!")
# fav_lenguaje()


# *args y **kwargs


#Args

# def suma(*args):
#     s = 0
#     for arg in args:
#         s += arg
#         return s
# suma(1,3,4,2)

# def suma(*args):
#     return sum(args)
# suma(5,5,3)

#Kwargs:

# def sumas(**kwargs):
#     se = 0
#     for key, value in kwargs.items():
#         print(key, "=", value)
#         se += value
#     return se
# sumas(a=3, b=10, c=3)

# def suma(*sumatoria):
#     return sum(sumatoria)
# suma(2,4,6,34.5)


# def suma (**evaluacion):
#     print(type(evaluacion))
# suma(x=3)
# def suma(**kwargs):
#     s = 0
#     for key, value in kwargs.items():
#         print(key, "=", value)
#         s += value
#     return s
    
# suma(a=3, b=10, c=3)

# def funcion(a, b, *args, **kwargs):
#     print("a =", a)
#     print("b =", b)
#     for arg in args:
#         print("args =", arg)
#     for key, value in kwargs.items():
#         print(key, "=", value)

# funcion(10, 20, 1, 2, 3, 4, x="Hola", y="Que", z="Tal")


#recursvidad

