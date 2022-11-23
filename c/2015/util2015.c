#ifndef _AOC_UTIL_2015_H_
#define _AOC_UTIL_2015_H_

#include "../util.h"
#include "util2015.h"

void parse(MAP* map, ARR_MUL_STRING* in) {
    map->values = (RECORD*) malloc(in->length * sizeof(RECORD));
    map->length = in->length;
    for (int16_t i = 0; i < in->length; i++) {
        if (in->strings[i].length == 3) {
            strcpy(map->values[i].function, "value");
            strcpy(map->values[i].key, in->strings[i].strings[2]);
            strcpy(map->values[i].value1, in->strings[i].strings[0]);
        } else if (in->strings[i].length == 4) {
            strcpy(map->values[i].key, in->strings[i].strings[3]);
            if (!strcmp(in->strings[i].strings[0], "NOT")) {
                strcpy(map->values[i].function, "not");
                strcpy(map->values[i].value1, in->strings[i].strings[1]);
            }
        } else if (in->strings[i].length == 5) {
            strcpy(map->values[i].key, in->strings[i].strings[4]);
            if (!strcmp(in->strings[i].strings[1], "AND")) {
                strcpy(map->values[i].function, "and");
                strcpy(map->values[i].value1, in->strings[i].strings[0]);
                strcpy(map->values[i].value2, in->strings[i].strings[2]);
            } else if (!strcmp(in->strings[i].strings[1], "OR")) {
                strcpy(map->values[i].function, "or");
                strcpy(map->values[i].value1, in->strings[i].strings[0]);
                strcpy(map->values[i].value2, in->strings[i].strings[2]);
            } else if (!strcmp(in->strings[i].strings[1], "LSHIFT")) {
                strcpy(map->values[i].function, "lshift");
                strcpy(map->values[i].value1, in->strings[i].strings[0]);
                strcpy(map->values[i].value2, in->strings[i].strings[2]);
            } else if (!strcmp(in->strings[i].strings[1], "RSHIFT")) {
                strcpy(map->values[i].function, "rshift");
                strcpy(map->values[i].value1, in->strings[i].strings[0]);
                strcpy(map->values[i].value2, in->strings[i].strings[2]);
            }
        }
    }
}

int16_t searchMap(MAP* map, char* key) {
    for (int16_t i = 0; i < map->length; i++) {
        if (!strcmp(map->values[i].key, key)) return i;
    }
    return -1;
}

bool isNumber(char* val) {
    bool ret = true;
    for (int16_t i = 0; i < strlen(val); i++) {
        ret &= val[i] >= '0' && val[i] <= '9';
    }
    return ret;
}

uint16_t evaluate(MAP* map, MAP* cache, char* key) {
    int16_t index = searchMap(cache, key);
    if (index != -1) return atoi(cache->values[index].value1);
    
    index = searchMap(map, key);
    if (index == -1) printf("ERROR: unknown index %d", index);
    RECORD r = map->values[index];
    uint16_t X, Y, retval = 0;
    if (!strcmp(r.function,"value")) {
        if (isNumber(r.value1)) {
            X = atoi(r.value1);
        } else {
            X = evaluate(map, cache, r.value1);
        }
        retval = X;
    } else if (!strcmp(r.function,"not")) {
        if (isNumber(r.value1)) {
            X = atoi(r.value1);
        } else {
            X = evaluate(map, cache, r.value1);
        }
        retval = ~X;
    } else if (!strcmp(r.function,"and")) {
        if (isNumber(r.value1)) {
            X = atoi(r.value1);
        } else {
            X = evaluate(map, cache, r.value1);
        }
        if (isNumber(r.value2)) {
            Y = atoi(r.value2);
        } else {
            Y = evaluate(map, cache, r.value2);
        }
        retval = X & Y;
    } else if (!strcmp(r.function,"or")) {
        if (isNumber(r.value1)) {
            X = atoi(r.value1);
        } else {
            X = evaluate(map, cache, r.value1);
        }
        if (isNumber(r.value2)) {
            Y = atoi(r.value2);
        } else {
            Y = evaluate(map, cache, r.value2);
        }
        retval = X | Y;
    } else if (!strcmp(r.function,"lshift")) {
        if (isNumber(r.value1)) {
            X = atoi(r.value1);
        } else {
            X = evaluate(map, cache, r.value1);
        }
        if (isNumber(r.value2)) {
            Y = atoi(r.value2);
        } else {
            Y = evaluate(map, cache, r.value2);
        }
        retval = X << Y;
    } else if (!strcmp(r.function,"rshift")) {
        if (isNumber(r.value1)) {
            X = atoi(r.value1);
        } else {
            X = evaluate(map, cache, r.value1);
        }
        if (isNumber(r.value2)) {
            Y = atoi(r.value2);
        } else {
            Y = evaluate(map, cache, r.value2);
        }
        retval = X >> Y;
    } else {
        printf("ERROR: unknown function %s\n", r.function);
    }
    index = searchMap(cache, key);
    if (index == -1) {
        index = cache->length;
        cache->length++;
    }
    char v[6];
    sprintf(v, "%u", retval);
    strcpy(cache->values[index].key, key);
    strcpy(cache->values[index].value1, v);
    return retval;
}

#endif //_AOC_UTIL_2015_H_