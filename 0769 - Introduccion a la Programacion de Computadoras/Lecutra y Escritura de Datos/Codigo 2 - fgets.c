#include<stdio.h> 
/*Este programa permite lee el contenido de un archivo, 
través de la función fgets. 
*/
int main() { 
    FILE *archivo; 
    char caracteres[50];
    archivo = fopen("gets.txt", "r");

    if (archivo != NULL) { 
        printf("El archivo se abrió correctamente. ");
        printf("\nContenido del archivo: \n");
        while (feof(archivo) ==0){ 
            fgets (caracteres,50, archivo); 
            printf(caracteres); 
        }
        fclose(archivo); 
    }
    return 0;
}