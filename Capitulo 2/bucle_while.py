#Inicializacion de la variable
contador = 0

#bucle while que se ejecuta mientras el contador sea menor que 5
while contador < 5:
	print(contador)
	contador += 1
print('fuera del bucle for')

#Pide al usuario que introduzca un numero positivo
numero = int(input("Introduce un numero positivo: "))

#Mientras el numero no sea positivo sigue pidiendo al usuario que ingrese un numero
while numero <=0:
	print("Eso no es un numero positivo. Intentelo de nuevo.")
	numero = int(input("Introduce otro numero positivo: "))

print(f"Has introducido un el numero positivo: {numero}")
