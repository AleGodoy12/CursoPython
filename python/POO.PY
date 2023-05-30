# POO
# Paradigmas de programacion
# Imperativo
# Declarativo
# Logico
# Funcional
# Orientado a objetos

# Como se piensa POOO
# Elemento principal : Auto | Clases
# Caracteristica: Modelo, color. | Atributos
# Funcionalidades: Reversa, andar, estacionar... | Metodos

# Definir clases
# class Perro:
#     pass
# miperro = Perro()
# Definir atributos
# Instancia
# class Perro:
#     def __init__(self, nombre, raza):
#         print(f"Creando perro {nombre}, {raza}")
#         self.nombre = nombre
#         self.raza = raza
# miperro = Perro("Toby", "Bulldog")
# print(type(miperro))
# print(miperro.nombre)
# print(miperro.raza)

# Clase
# class Perro:
#     especie = "mamifero"
#     def __init__(self, nombre, raza):
#         print(f"Creando perro {nombre}, {raza}")
        
#         self.nombre = nombre
#         self.raza = raza
# print(Perro.especie)
# Perro.especie

# Metodos
# class Perro:
#     especie = "mamifero"
#     def __init__(self, nombre, raza):
#         print(f"Creando perro {nombre}, {raza}")
        
#         self.nombre = nombre
#         self.raza = raza
#     def ladra(self):
#         print("guau")
#     def camina(self, pasos):
#         print(f"Caminando {pasos} pasos")
# miperro = Perro("Toby", "Bulldog")
# miperro.ladra()
# miperro.camina(10)

# class Clase:
#     def metodo(self):
#         return "metodo normal", self
#     @classmethod
#     def metododeclase(cls):
#         return "metodo de clase", cls
#     @staticmethod
#     def metodoestativo():
#         return "metodo estatico"

# class Clase:
#     def metodo(self, arg1, arg2):
#         return "metodo normal", self
# miclase = Clase()
# miclase.metodo("a","b")

# metodos de clases classmethod

# class Clase:
#     @classmethod
#     def metododeclase(cls):
#         return "metodo de clase", cls
# Clase.metododeclase()

# Metodos estaticos  staticmethod
# class Clase:
#     @staticmethod
#     def metodoestatico():
#         return "Metodo estativo"
# miclase = Clase()

# Herencia
# class Animal:
#     def __init__(self, especie, edad):
#         self.especie = especie
#         self.edad = edad
#     def hablar(self):
#         pass
#     def moverse(self):
#         pass
#     def describeme(self):
#         print("Soy un animal del tipo", type(self).__name__)
# class Perro(Animal):
#     pass
# miperro = Perro("mamifero", 10)
# miperro.describeme()

# class Perro(Animal):
#     def hablar(self):
#         print("Guau")
#     def moverse(self):
#         print("caminando con 4 patas")
# class Vaca(Animal):
#     def hablar(self):
#         print("Muuu!")
#     def moverse(self):
#         print("Caminando con 4 patas")
# class abeja(Animal):
#     def hablar(self):
#         print("Bzzz!")
#     def moverse(self):
#         print("Volando")
#     def picar(self):
#         print("Picar!")
# miperro = Perro("Mamifero", 10)
# mivaca = Vaca("Mamifero", 20)
# miabeja = abeja("Insecto", 1)

# miperro.hablar()
# mivaca.hablar()
# mivaca.describeme()
# miabeja.describeme()
# miabeja.picar()

# Super()
# class Animal:
#     def __init__(self, especie, edad, dueño):
#         self.especie = especie
#         self.edad = edad
#         super().__init__(especie, edad)
#         self.dueño = dueño
#     def hablar(self):
#         pass
#     def moverse(self):
#         pass
#     def describeme(self):
#         print("Soy un animal del tipo", type(self).__name__)


#Polimorfismo 
#Poly de muchos y morfo de formas
# class Animal:
#     def hablar(self):
#         pass
# class Perro(Animal):
#     def hablar(self):
#         print("Guau")
# class Gato(Animal):
#     def hablar(self):
#         print("Miau")
# for animal in Perro(), Gato():
#     animal.hablar()

# class Marino():
#     def hablar(self):
#      print("Hola..")
# class Pulpo(Marino):
#     def hablar(self):
#         print("Soy un pulpo")
# class Foca(Marino):
#     def hablar(self, mensaje):
#         print(mensaje)
        
# pulpito = Pulpo()
# Foquita = Foca()
# pulpito.hablar()
# Foquita.hablar("Soy una foca, este es mi mensaje")

    
#Encapsulamiento

class Clase:
    atributo_clase = "Hola"
    def __init__(self, atributo_instancia):
        self.atributo_instancia = atributo_instancia
mi_clase = Clase("Que tal?")
mi_clase.atributo_clase
mi_clase.atributo_instancia

class Clase:
    atributo_clase = "Hola" # accesible desde el exterior
    __atributo_clase = "Hola" #No es accesible
    
    def __mi_metodo(self):
        print("Haz algo")
        self.__variable = 0
    def metodo_normal(self):
        self.__mi_metodo()
mi_clase = Clase()
