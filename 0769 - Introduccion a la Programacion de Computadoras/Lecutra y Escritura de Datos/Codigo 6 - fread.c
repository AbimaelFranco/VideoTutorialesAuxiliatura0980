#include <stdio.h> 
/* Este programa muestra el contenido de un archivo de texto. El nombre del archivo se recibe como argumento de la función principal. */ 

int main(int argc, char **argv) { 
    FILE *ap; 
    unsigned char buffer[2048]; // Buffer de 2 Kbytes 
    int bytesLeidos; 
    
    // Si no se ejecuta el programa correctamente 
    if(argc < 2) { 
        printf("Ejecutar el programa de la siguiente manera:\n\tnombre_\tprograma nombre_archivo\n"); 
        return 1; 
    } 
    // Se abre el archivo de entrada en modo lectura y binario 
    ap = fopen(argv[1], "rb"); 
    if(!ap) { 
        printf("El archivo %s no existe o no se puede abrir", argv[1]); 
        return 1; 
    } 
    while(bytesLeidos = fread(buffer, 1, 2048, ap)) 
    printf("%s", buffer); 
    
    fclose(ap); 
    return 0; 
}