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

ARR_STRING* readInput(char* file) {
    ARR_STRING* arr = malloc(sizeof(ARR_STRING));

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
    arr->strings = input;
    arr->length = i;
    return arr;
}

ARR_MUL_STRING* readInputDelimiter(char* file, char delimiter) {
    ARR_MUL_STRING* mulInput = malloc(sizeof(ARR_MUL_STRING));
    ARR_STRING* input = readInput(file);
    
    mulInput->length = input->length;
    for (int16_t i = 0; i < input->length; i++) {
        ARR_STRING* line = malloc(sizeof(ARR_STRING));


        freeArrString(line);
    }

    freeArrString(input);
    return mulInput;
}

ARR_INTEGER* readIntInput(char* file) {
    ARR_INTEGER* intInput = malloc(sizeof(ARR_INTEGER));
    ARR_STRING* input = readInput(file);

    intInput->length = input->length;
    intInput->integers = malloc(input->length * sizeof(int16_t));
    for (int16_t i = 0; i < input->length; i++) {
        intInput->integers[i] = atoi(input->strings[i]);
    }

    freeArrString(input);
    return intInput;
}

void freeArrString(ARR_STRING* input) {
    for (int16_t i = 0; i < input->length; i++) {
        free(input->strings[i]);
    }
    free(input->strings);
    free(input);
}

void freeArrInteger(ARR_INTEGER* input) {
    free(input->integers);
    free(input);
}
