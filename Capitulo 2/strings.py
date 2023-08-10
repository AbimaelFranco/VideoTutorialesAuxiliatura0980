print('1. Indexacion de los strings:')
s = "Hola Mundo"
print(s[0])
print(s[4])
print(s[-1])

print('2. Cortar un string (Slicing):')
s = "Hola Mundo"
print(s[0:4])
print(s[5:])

print('3. Concatenar strings:')
s1 = "Hola"
s2 = "Mundo"
s3 = s1 + " " + s2
print(s3)

print('4. Cambiar un valor en un string:')
s = "Hola Mundo"
s = s.replace("H", "h")
print(s)

s = "Hola Mundo"
print(s.upper())
print(s.lower())
print(s.replace("H", "h"))
print(s.lstrip())
print(s.rstrip())
print(s.strip())
print(s.split())