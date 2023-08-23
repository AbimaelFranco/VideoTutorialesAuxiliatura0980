#include <stdio.h> 
/* Este programa realizar una copia exacta de dos archivos. Los nombres de los archivos (origen y destino) se reciben como argumentos de la función principal. */ 

int main(int argc, char **argv) { 
    FILE *archEntrada, *archivoSalida; 
    unsigned char buffer[2048]; // Buffer de 2 Kbytes 
    int bytesLeidos; 
    
    // Si no se ejecuta el programa correctamente 
    if(argc < 3) { 
        printf("Ejectuar el programa de la siguiente manera:\n"); 
        printf("\tnombre_programa \tarchivo_origen \tarchivo_destino\n"); 
        return 1; 
    } 

    // Se abre el archivo de entrada en modo de lectura y binario 
    archEntrada = fopen(argv[1], "rb"); 
    if(!archEntrada) { 
        printf("El archivo %s no existe o no se puede abrir", argv[1]); 
        return 1; 
    } 
            
    // Se crea o sobreescribe el archivo de salida en modo binario 
    archivoSalida = fopen(argv[2], "wb"); 

    if(!archivoSalida) { 
        printf("El archivo %s no puede ser creado", argv[2]);
        return 1; 
    } 

    // Copia archivos 
    while (bytesLeidos = fread(buffer, 1, 2048, archEntrada)) 
    fwrite(buffer, 1, bytesLeidos, archivoSalida); 
    
    // Cerrar archivos 
    fclose(archEntrada); 
    fclose(archivoSalida); 
    return 0; 
}