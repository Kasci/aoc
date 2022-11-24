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
        input[i] = (char *) malloc(strlen(buf) + 5);
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

ARR_MUL_INTEGERS* readIntInputDelim(char* file, char* delimiters) {
    ARR_MUL_INTEGERS* mulInput = (ARR_MUL_INTEGERS*) malloc(sizeof(ARR_MUL_INTEGERS));
    ARR_STRING* input = readInput(file);
    
    mulInput->length = input->length;
    mulInput->integers = (ARR_INTEGER*) malloc(input->length * sizeof(ARR_INTEGER));
    for (int16_t i = 0; i < input->length; i++) {
        ARR_INTEGER line;
        line.integers = (int16_t*) malloc(0);
        int16_t j = 0;
        char* point = strtok(input->strings[i], delimiters);
        while (point != NULL) {
            line.integers = (int16_t*) realloc(line.integers, (j+1)*sizeof(int16_t));
            line.integers[j] = atoi(point);
            point = strtok(NULL, delimiters);
            j++;
        }
        line.length = j;
        mulInput->integers[i] = line;
    }

    freeArrString(input);
    return mulInput;
}

ARR_MUL_INTEGERS* initMulIntegers(int16_t arraySize, int16_t listSize) {
    ARR_MUL_INTEGERS* mulInput = (ARR_MUL_INTEGERS*) malloc(sizeof(ARR_MUL_INTEGERS));
    mulInput->length = arraySize;
    mulInput->integers = (ARR_INTEGER*) malloc(arraySize * sizeof(ARR_INTEGER));
    for (int16_t i = 0; i < arraySize; i++) {
        mulInput->integers[i].length = listSize;
        mulInput->integers[i].integers = (int16_t*) malloc(listSize * sizeof(int16_t));
        for (int16_t j = 0; j < listSize; j++) {
            mulInput->integers[i].integers[j] = 0;
        }
        printf(". %d\n",i);
    }
    return mulInput;
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

void freeArrMulInteger(ARR_MUL_INTEGERS* input) {
    for (int16_t i = 0; i < input->length; i++) {
        free(input->integers[i].integers);
    }
    free(input->integers);
    free(input);
}

bool comparePoints(POINT a, POINT b) {
    return a.x == b.x && a.y == b.y && a.z == b.z;
}

#define DEPTH_INC 32

STACK* initStack(size_t size) {
    STACK* s = (STACK*) malloc(sizeof(STACK));
    s->count = 0;
    s->depth = DEPTH_INC;
    s->items = (void**) malloc(s->depth * size);
    return s;
}

void pushItemStack(STACK* stack, void* item, size_t size) {
    if (stack->count + 1 >= stack->depth) {
        stack->depth += DEPTH_INC;
        stack->items = (void**) realloc(stack->items, stack->depth * size);
    }
    memcpy(stack->items[stack->count], item, size);
    stack->count++;
}

void* popItemStack(STACK* stack, size_t size) {
    void* item = stack->items[stack->count];
    stack->count--;
    if (stack->count <= stack->depth - DEPTH_INC) {
        stack->depth -= DEPTH_INC;
        stack->items = (void**) realloc(stack->items, stack->depth * size);
    }
    return item;
}

void freeStack(STACK* stack) {
    free(stack->items);
    free(stack);
}
