print('1. Ejemplo diccionario:')
#Definicion de un diccionario
mi_diccionario = {"clave1": "valor1", "clave2": "valor2", "clave3": "valor3"}
print(mi_diccionario)

print('2. Acceder a un valor de una clave:')
print(mi_diccionario["clave1"])

print('3. Asignar un nuevo valor a una clave:')
mi_diccionario["clave1"] = "Nuevo valor1"
print(mi_diccionario)

print('4. Iteracion de un diccionario:')
for clave, valor in mi_diccionario.items():
    print(f"La cavles es '{clave}' y el valor es '{valor}'")

print('5. Metodos de los diccionarios:')
mi_diccionario.clear()
print(mi_diccionario)

mi_diccionario = {"clave1": "valor1", "clave2": "valor2", "clave3": "valor3"}
nuevo_diccionario = mi_diccionario.copy()
print(mi_diccionario)

#crea un nuevo diccionario con las claves dadas y el mismo valor
claves = ('clave1', 'clave2', 'clave')
valor = 'valor'
diccionario_fromkeys = dict.fromkeys(claves, valor)
print(diccionario_fromkeys)

#Devuelve el valor para la clave especificada si existe
print(mi_diccionario.get("clave1"))

#Comprueba si la clave especificada existe en el diccionario
print("clave1" in mi_diccionario)

#Devuelve una lista de todos los pares claves-valor
print(mi_diccionario.items())

#Devuelve una lista con todas las claves
print(mi_diccionario.keys())

#Actualiza el diccionario con los pares clave-valor especificados
mi_diccionario.update({"clave1":"nuevo valor1", "clave4": "valor4"})
print(mi_diccionario)

#Devuelve una lista con todos los valores
print(mi_diccionario.values())