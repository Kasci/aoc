typedef struct record {
    char key[6];
    char function[10];
    char value1[6];
    char value2[6];
} RECORD;

typedef struct map {
    RECORD* values;
    int16_t length;
} MAP;

#include "../util.h"

void parse(MAP* map, ARR_MUL_STRING* in);
int16_t searchMap(MAP* map, char* key);
uint16_t evaluate(MAP* map, MAP* cache, char* key);