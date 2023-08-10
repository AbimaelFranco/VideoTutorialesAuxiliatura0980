#Objetos numericos
##Escalares
375
3.75e2
3.75E2
0x177

##Rangos
###numero_inicial:salto:numero_final
1:10
1:0.5:10
1:1.5:10
1:1.6:10

##Matrices
M = [1, 2, 3; 4, 5, 6; 7, 8, 9]
M = [1:3; 4:6; 7:9]

##Strings
"Cadena"
'Cadena'
"\a"  #Sonido de windows

##Estructuras
x = {}
x.secuencia = 1:5
x.matriz = [1, 2; 44,5]
x.string = 'secuencia'
x.estructura = {}
x.estructura.numero = 0x177
x.estructura.letra = 'A'
x

##Operadores Aritmeticos
x = 2
y = 3
x + y
x - y
x * y
x / y
++x
--x

##Operadores de Comparacion
x < y
x <= y
x == y
x > y
x >= y
x != y

##Tipos de Operadores Booleanos
x = 1
y = 0
x & y
x | y
not(x)

##Estructuras de Flujo
if (x>y)
  printf('x es mayor a y \n')
elseif x==y
  printf('x es igual a y \n')
else
  printf('x es menor a y \n')
endif

x=0
y=5
z=0
while(z < y)
  printf('el valor de z es: ', z)
  ++z
endwhile

fib = ones(1, 10)
for i = 3:10
  fib(i) = fib(i-1) + fib(i-2);
endfor
fib

try
  m = [1:5; 10:15]
catch
  'Error, no se puede ejecutar'
end_try_catch

##Operaciones basicas con matrices
M = [1, 2, 7; 4, 5, 11; 0.1, 0.2, 0.3]
N = [0, 1, 2; 8, 10, 12; 0x177, 0x176, 0x125]

M+N
M-N
#M * N
cross(M,N)  #MxN
dot(M,N)    #M○N
M'
