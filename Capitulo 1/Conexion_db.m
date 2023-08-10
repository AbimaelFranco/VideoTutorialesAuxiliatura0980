pkg load database
conn = pq_connect(setdbopts('dbname', 'auxiliatura0980', 'host', 'localhost', 'port', '5433', 'user', 'postgres', 'password', 'pass'))

###Insertar registro
N = pq_exec_params(conn, "Insert INTO ejemplo (id, nombre, apellido) VALUES (1, 'Alexander', 'Sanan');");

###Eliminar registro que cumpla filtro
##N = pq_exec_params(conn, "DELETE FROM ejemplo where ID = 1;");

###Modificar registro que cumpla filtro
##N = pq_exec_params(conn, "UPDATE ejemplo set ID = 25 where Nombre = 'Alexander';");

###Obtener todos los registros de una tabla
N = pq_exec_params(conn, "SELECT * FROM ejemplo;");

##printf("Toda la estructura de la db: \n");
##N

##printf("Solo la data de la db: \n");
##N.data

printf("Obtencion de informacion de un registro: \n");
ID = cell2mat(N.data(1, 1));
Nombre = cell2mat(N.data(1, 2));
Apellido = num2str(cell2mat(N.data(1, 3)));

output_str = ["El ID del estudiante ", Nombre, " ", Apellido, " es: ", num2str(ID)];
disp(output_str);
