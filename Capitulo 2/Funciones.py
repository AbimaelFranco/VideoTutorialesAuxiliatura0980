def procesar_datos(numero, cadena, lista):
    ##Funcion que toma un numero entero, una cadena y una lista y realiza operaciones

    #Dobla el numero
    numero = numero*2

    #convierte la cadena en mayusculas
    cadena = cadena.upper()

    #añade un elemento a la lista
    lista.append("Nuevo elemento")

    #Devuelve los valores
    return numero, cadena, lista

#Enviar datos a la funcion y recibir datos de la funcion
mi_numero = 5
mi_cadena = "Hola mundo"
mi_lista = ["elemento1", "elmento2"]

nuevo_numero, nueva_cadena, nueva_lista = procesar_datos(mi_numero, mi_cadena, mi_lista)

print(f"El nuevo numero es {nuevo_numero}")
print(f"La nueva cadena es {nueva_cadena}")
print(f"La nueva lista es {nueva_lista}")