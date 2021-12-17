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

ARR_STRING* readInput(char* file);
void freeInput(ARR_STRING* input);

ARR_INTEGER* readIntInput(char* file);
void freeIntInput(ARR_INTEGER* input);

#endif //_AOC_UTIL_H_
