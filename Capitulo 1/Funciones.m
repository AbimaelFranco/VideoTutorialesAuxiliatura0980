#Funciones
#h = hipotenusa(3, 4)
##[h, angle] = hipotenusa(3, 4)

##x = [-3:0.1:1];
#Una alternativa a este comando es: linspace(inicio, final, cantidad_puntos)
##x = linspace(-3, 1, 50)
##plot(x, funcion(x), 'color', 'red', 'LineStyle', ':');
##title('Titulo')
##xlabel('etiqueta x')
##ylabel('etiqueta y')

#Para ploteos discretos se utiliza la funcion stem
##stem(x, funcion(x), 'color', 'red', 'LineStyle', ':');
##legend('funcion')

#Graficacion de funciones seno y coseno de forma simultanea
x = [0:0.1:4*pi];
y1 = sin(x);
y2 = cos(x);
hold on; #Para que no plotee hasta finalizar
p1 = plot(x, y1);
p2 = plot(x, y2);
set(p1, 'Color', 'red', 'LineWidth', 2)
set(p2, 'Color', 'blue', 'LineWidth', 1)
xlabel('Eje X');
ylabel('Eje Y');
title('Grafica de seno y coseno');
legend('seno', 'coseno');
hold off;
