#ifndef _AOC_UTIL_H_
#define _AOC_UTIL_H_

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdbool.h>
#include <string.h>
#include <stdint.h>
#include <assert.h>

typedef struct strArr {
    char** strings;
    int16_t length;
} ARR_STRING;

typedef struct strMulArr {
    ARR_STRING* strings;
    int16_t length;
} ARR_MUL_STRING;

typedef struct intArr {
    int16_t* integers;
    int16_t length;
} ARR_INTEGER;

typedef struct intMulArr {
    ARR_INTEGER* integers;
    int16_t length;
} ARR_MUL_INTEGERS;

typedef struct pointObj {
    int16_t x;
    int16_t y;
    int16_t z;
} POINT;

typedef struct stackObj {
    int32_t depth;
    int32_t count;
    void** items;
} STACK;

ARR_STRING* readInput(char* file);
void freeArrString(ARR_STRING* input);

ARR_MUL_STRING* readInputDelim(char* file, char* delimiters);
void freeArrMulString(ARR_MUL_STRING* input);

ARR_INTEGER* readIntInput(char* file);
void freeArrInteger(ARR_INTEGER* input);

ARR_MUL_INTEGERS* readIntInputDelim(char* file, char* delimiters);
void freeArrMulInteger(ARR_MUL_INTEGERS* input);

ARR_MUL_INTEGERS* initMulIntegers(int16_t arraySize, int16_t listSize);

bool comparePoints(POINT a, POINT b);

STACK* initStack(size_t size);
void pushItemStack(STACK* stack, void* item, size_t size);
void* popItemStack(STACK* stack, size_t size);
void freeStack(STACK* stack);

bool isIn(char* val, char** arr, int16_t maxIdx);

#endif //_AOC_UTIL_H_
