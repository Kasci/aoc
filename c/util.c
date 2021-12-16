#include "util.h"

bool isWhite(char c) {
    return c == ' ' || c == '\n' || c == '\t' || c == '\r';
}

char* trim(char* input) {
    while (isWhite(*input)) input++;
    char* back = input + strlen(input) - 1;
    while (isWhite(*back)) --back;
    *(back+1) = '\0';
    return input;
}

char** readInput(char* file) {
    FILE *file_ptr = fopen(file, "r");
    if (file_ptr == NULL) {
        perror("Error opening file");
        exit(1);
    }
    
    char buf[255];
    char **input = (char **) malloc(0);
    int16_t i = 0;
    
    while(fgets(buf, 255, (FILE*)file_ptr) != NULL) {
        strcpy(buf, trim(buf));
        input = (char **) realloc(input, (i+1)*sizeof(char *));
        input[i] = (char *) malloc(strlen(buf));
        strcpy(input[i],buf);
        i++;
    } 
    fclose(file_ptr);
    return input;
}

void freeInput(char** input) {
    int16_t size = sizeof(input)/sizeof(char *);
    for (int16_t i = 0; i < size; i++) {
        free(input[i]);
    }
    free(input);
}
