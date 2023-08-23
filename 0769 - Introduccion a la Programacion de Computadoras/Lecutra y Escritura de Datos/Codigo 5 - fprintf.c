#include<stdio.h> 
/* Este programa permite escribir dentro de un archivo, de ser posible, a través de la función fprintf. */ 
int main() { 
    FILE *archivo; 
    char escribir[] = "Escribir cadena en archivo mediante fprinft. \nFacultad de Ingeniería.\n"; 
    archivo = fopen("fprintf.txt", "r+"); 
    if (archivo != NULL) { fprintf(archivo, escribir); 
    fprintf(archivo, "%s", "UNAM\n"); 
    fclose(archivo); 
    } else { 
        printf("El archivo no existe o no se tiene permisos de lectura / escritura.\n"); 
    } 
    return 0; 
}