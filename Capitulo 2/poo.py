class MiClase:
    #Atributo de clase
    atributo_clase = "Soy un atributo de clase"

    def __init__(self, nombre, edad):
        #Atributos del objeto
        self.nombre = nombre
        self.edad = edad

    #Metodo de instancia
    def saludar(self):
        return f"Hola, mi nombre es {self.nombre} y teno {self.edad} años."
    
    #Metodo de clase (decorador @classmethod)
    @classmethod
    def metodo_clase(cls):
        return f"Este es un metodo de clase. {cls.atributo_clase}"
    
    #Metodo estatico(decorador @staticmethod)
    @staticmethod
    def metodo_estatico():
        return "Este es un metodo estatico"
    
#Crear una instancia de la calse
objeto1 = MiClase("Juan", 30)

#Acceder a los atributos del objeto
print(objeto1.nombre)
print(objeto1.edad)

#Llamar a un metodo de instancia
saludo = objeto1.saludar()
print(saludo)

#Acceder al atributo de clase desde la instancia
print(objeto1.atributo_clase)

#Llamar al metodo de clase desde la instancia
resultado_metodo_clase = objeto1.metodo_clase()
print(resultado_metodo_clase)

#Llamar al metodo estatico desde la instancia
resultado_metodo_estatico = objeto1.metodo_estatico()
print(resultado_metodo_estatico)

#Llamar al metodo de clase directamente desde la clase (sin necesidad de instancia)
resultado_metodo_clase2 = MiClase.metodo_clase()
print(resultado_metodo_clase2)

#Llamar al metodo estatico directamente desde la clase (sin necesidad de instancia)
resultado_metodo_estatico2 = MiClase.metodo_estatico()
print(resultado_metodo_estatico2)