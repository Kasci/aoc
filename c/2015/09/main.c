#include "../../util.h"

#if 0
static char *FILE_NAME = "sample.txt";
#else
static char *FILE_NAME = "input.txt";
#endif

typedef struct route {
    char a[20];
    char b[20];
    int64_t path;
} ROUTE;

int64_t path1(int8_t size, int8_t usedIdx, char* used[], ROUTE all[], int64_t sum) {
    char* last = used[usedIdx-1];
    int8_t idx = 0;
    ROUTE routes[size];
    int8_t nextIdx = 0;
    ROUTE allNext[size];
    for (int16_t i = 0; i < size; i++) {
        ROUTE r = all[i];
        if (!isIn(r.a, used, usedIdx-1) && !isIn(r.b, used, usedIdx-1)) {
            strcpy(allNext[nextIdx].a, all[i].a);
            strcpy(allNext[nextIdx].b, all[i].b);
            allNext[nextIdx].path = all[i].path;
            nextIdx++;
        }
    }
    for (int16_t i = 0; i < nextIdx; i++) {
        if (!strcmp(last, allNext[i].a)) {
            strcpy(routes[idx].a, allNext[i].a);
            strcpy(routes[idx].b, allNext[i].b);
            routes[idx].path = allNext[i].path;
            idx++;
        } else if (!strcmp(last, allNext[i].b)) {
            strcpy(routes[idx].a, allNext[i].b);
            strcpy(routes[idx].b, allNext[i].a);
            routes[idx].path = allNext[i].path;
            idx++;
        }
    }
    if (idx == 0) {
        return sum;
    } else {
        int64_t min = 9999;
        for (int16_t i = 0; i < idx; i++) {
            char **usedNext = malloc((usedIdx+1)*sizeof(char*));
            for (int16_t j = 0; j < usedIdx; j++) {
                usedNext[j] = malloc(200 * sizeof(char));
                strcpy(usedNext[j], used[j]);
            }
            usedNext[usedIdx] = malloc(200 * sizeof(char));
            strcpy(usedNext[usedIdx], routes[i].b);
            int64_t ret = path1(nextIdx, usedIdx+1, usedNext, allNext, sum + routes[i].path);
            if (ret < min) {
                min = ret;
            }
            for (int16_t j = 0; j < usedIdx+1; j++) {
                free(usedNext[j]);
            }
            free(usedNext);
        }
        return min;
    }
}

int64_t path2(int8_t size, int8_t usedIdx, char* used[], ROUTE all[], int64_t sum) {
    char* last = used[usedIdx-1];
    int8_t idx = 0;
    ROUTE routes[size];
    int8_t nextIdx = 0;
    ROUTE allNext[size];
    for (int16_t i = 0; i < size; i++) {
        ROUTE r = all[i];
        if (!isIn(r.a, used, usedIdx-1) && !isIn(r.b, used, usedIdx-1)) {
            strcpy(allNext[nextIdx].a, all[i].a);
            strcpy(allNext[nextIdx].b, all[i].b);
            allNext[nextIdx].path = all[i].path;
            nextIdx++;
        }
    }
    for (int16_t i = 0; i < nextIdx; i++) {
        if (!strcmp(last, allNext[i].a)) {
            strcpy(routes[idx].a, allNext[i].a);
            strcpy(routes[idx].b, allNext[i].b);
            routes[idx].path = allNext[i].path;
            idx++;
        } else if (!strcmp(last, allNext[i].b)) {
            strcpy(routes[idx].a, allNext[i].b);
            strcpy(routes[idx].b, allNext[i].a);
            routes[idx].path = allNext[i].path;
            idx++;
        }
    }
    if (idx == 0) {
        return sum;
    } else {
        int64_t max = -1;
        for (int16_t i = 0; i < idx; i++) {
            char **usedNext = malloc((usedIdx+1)*sizeof(char*));
            for (int16_t j = 0; j < usedIdx; j++) {
                usedNext[j] = malloc(200 * sizeof(char));
                strcpy(usedNext[j], used[j]);
            }
            usedNext[usedIdx] = malloc(200 * sizeof(char));
            strcpy(usedNext[usedIdx], routes[i].b);
            int64_t ret = path2(nextIdx, usedIdx+1, usedNext, allNext, sum + routes[i].path);
            if (ret > max) {
                max = ret;
            }
            for (int16_t j = 0; j < usedIdx+1; j++) {
                free(usedNext[j]);
            }
            free(usedNext);
        }
        return max;
    }
}


void part1() {
    ARR_MUL_STRING* in = readInputDelim(FILE_NAME, " ");
    int64_t k = 9999;
    char **names;
    names = (char**) malloc(20 * sizeof(char[10]));
    int16_t idx = 0;
    ROUTE routes[in->length];
    for (int16_t i = 0; i < in->length; i++) {
        char* c = in->strings[i].strings[0];
        if (!isIn(c, names, idx)) {
            names[idx] = malloc(sizeof(char[20]));
            strcpy(names[idx++], c);
        }
        strcpy(routes[i].a, c);
        c = in->strings[i].strings[2];
        if (!isIn(c, names, idx)) {
            names[idx] = malloc(sizeof(char[20]));
            strcpy(names[idx++], c);
        }
        strcpy(routes[i].b, c);
        routes[i].path = atoi(in->strings[i].strings[4]);
    }
    for (int16_t i = 0; i < idx; i++) {
        char* used[] = {names[i]};
        int64_t out = path1(in->length, 1, used, routes, 0);
        // printf("> %d\n", out);
        if (out < k) {
            k = out;
        }
    }
    printf("Part 1: %ld\n", k);
    for (int16_t i = 0; i < idx; i++) {
        free(names[i]);
    }
    free(names);
    freeArrMulString(in);
}

void part2() {
    ARR_MUL_STRING* in = readInputDelim(FILE_NAME, " ");
    int64_t k = -1;
    char **names;
    names = (char**) malloc(20 * sizeof(char[10]));
    int16_t idx = 0;
    ROUTE routes[in->length];
    for (int16_t i = 0; i < in->length; i++) {
        char* c = in->strings[i].strings[0];
        if (!isIn(c, names, idx)) {
            names[idx] = malloc(sizeof(char[20]));
            strcpy(names[idx++], c);
        }
        strcpy(routes[i].a, c);
        c = in->strings[i].strings[2];
        if (!isIn(c, names, idx)) {
            names[idx] = malloc(sizeof(char[20]));
            strcpy(names[idx++], c);
        }
        strcpy(routes[i].b, c);
        routes[i].path = atoi(in->strings[i].strings[4]);
    }
    for (int16_t i = 0; i < idx; i++) {
        char* used[] = {names[i]};
        int64_t out = path2(in->length, 1, used, routes, 0);
        if (out > k) {
            k = out;
        }
    }
    printf("Part 2: %ld\n", k);
    for (int16_t i = 0; i < idx; i++) {
        free(names[i]);
    }
    free(names);
    freeArrMulString(in);
}

int main(void) {
    part1();
    part2();
    return 0;
}
