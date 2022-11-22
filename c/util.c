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

#define LEN 5000

ARR_STRING* readInput(char* file) {
    ARR_STRING* arr = malloc(sizeof(ARR_STRING));

    FILE *file_ptr = fopen(file, "r");
    if (file_ptr == NULL) {
        perror("Error opening file");
        exit(1);
    }
    
    char buf[LEN];
    char **input = (char **) malloc(0);
    int16_t i = 0;
    
    while(fgets(buf, LEN, (FILE*)file_ptr) != NULL) {
        strcpy(buf, trim(buf));
        input = (char **) realloc(input, (i+1)*sizeof(char *));
        input[i] = (char *) malloc(strlen(buf));
        strcpy(input[i],buf);
        while (strlen(buf) == LEN-1) {
            fgets(buf, LEN, (FILE*)file_ptr);
            strcpy(buf, trim(buf));
            input[i] = (char *) realloc(input[i], strlen(input[i]) + strlen(buf) + 1);
            char* ptr = input[i];
            ptr += strlen(input[i]);
            strcpy(ptr, buf);
        }
        i++;
    } 
    fclose(file_ptr);
    arr->strings = input;
    arr->length = i;
    return arr;
}

ARR_MUL_STRING* readInputDelim(char* file, char* delimiters) {
    ARR_MUL_STRING* mulInput = (ARR_MUL_STRING*) malloc(sizeof(ARR_MUL_STRING));
    ARR_STRING* input = readInput(file);
    
    mulInput->length = input->length;
    mulInput->strings = (ARR_STRING*) malloc(input->length * sizeof(ARR_STRING));
    for (int16_t i = 0; i < input->length; i++) {
        ARR_STRING line;
        line.strings = (char**) malloc(0);
        int16_t j = 0;
        char* point = strtok(input->strings[i], delimiters);
        while (point != NULL) {
            line.strings = (char**) realloc(line.strings, (j+1)*sizeof(char*));
            line.strings[j] = (char*) malloc(strlen(point));
            strcpy(line.strings[j], point);
            point = strtok(NULL, delimiters);
            j++;
        }
        line.length = j;
        mulInput->strings[i] = line;
    }

    freeArrString(input);
    return mulInput;
}

ARR_INTEGER* readIntInput(char* file) {
    ARR_INTEGER* intInput = (ARR_INTEGER*) malloc(sizeof(ARR_INTEGER));
    ARR_STRING* input = readInput(file);

    intInput->length = input->length;
    intInput->integers = (int16_t*) malloc(input->length * sizeof(int16_t));
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

void freeArrStringDirect(ARR_STRING input) {
    for (int16_t i = 0; i < input.length; i++) {
        free(input.strings[i]);
    }
    free(input.strings);
}

void freeArrMulString(ARR_MUL_STRING* input) {
    for (int16_t i = 0; i < input->length; i++) {
        freeArrStringDirect(input->strings[i]);
    }
    free(input->strings);
    free(input);
}
