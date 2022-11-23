#include "../../util.h"
#include "../util2015.h"

#if 0
static char *FILE_NAME = "sample.txt";
#else
static char *FILE_NAME = "input.txt";
#endif


void part1() {
    ARR_MUL_STRING* in = readInputDelim(FILE_NAME, " ");
    int64_t k = 0;
    MAP map;
    parse(&map, in);
    MAP cache;
    cache.values = (RECORD*) malloc(in->length * sizeof(RECORD));
    cache.length = 0;
    printf("Part 1: %ld\n", evaluate(&map, &cache, "a"));
    free(map.values);
    free(cache.values);
    freeArrMulString(in);
}

void part2() {
    ARR_MUL_STRING* in = readInputDelim(FILE_NAME, " ");
    int64_t k = 0;
    MAP map;
    parse(&map, in);
    int16_t index = searchMap(&map, "b");
    strcpy(map.values[index].function, "value");
    strcpy(map.values[index].value1, "46065");
    MAP cache;
    cache.values = (RECORD*) malloc(in->length * sizeof(RECORD));
    cache.length = 0;
    printf("Part 2: %ld\n", evaluate(&map, &cache, "a"));
    free(map.values);
    free(cache.values);
    freeArrMulString(in);
}

int main(void) {
    part1();
    part2();
    return 0;
}
