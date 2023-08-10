#Definicion de clase base
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def saludar(self):
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años."
    
#Definicion de clase derivada (hija)
class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        #Usa la funcion super() para llamar al __init__ de la clase base
        super().__init__(nombre, edad)
        #Atributo adicional de la clase estudiante
        self.grado = grado

    #Extension del metodo saludar
    def saludar(self):
        saludo_base = super().saludar()
        return f"{saludo_base} Estoy estudiando {self.grado}."

#Crear una instancia de la clase estudiante
estudiante1 = Estudiante("Juan", 20, "Informatica")

#Llamar al metodo saludar
saludo = estudiante1.saludar()
print(saludo)