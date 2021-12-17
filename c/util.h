#ifndef _AOC_UTIL_H_
#define _AOC_UTIL_H_

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdbool.h>
#include <string.h>
#include <stdint.h>
#include <assert.h>

typedef struct intArr {
    int16_t* integers;
    int16_t length;
} ARR_INTEGER;

typedef struct strArr {
    char** strings;
    int16_t length;
} ARR_STRING;

typedef struct strMulArr {
    ARR_STRING* strings;
    int16_t length;
} ARR_MUL_STRING;

ARR_STRING* readInput(char* file);
void freeArrString(ARR_STRING* input);

ARR_MUL_STRING* readInputDelim(char* file, char delimiter);
void freeArrMulString(ARR_MUL_STRING* input);

ARR_INTEGER* readIntInput(char* file);
void freeArrInteger(ARR_INTEGER* input);

#endif //_AOC_UTIL_H_
