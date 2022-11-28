#include "../../util.h"

#if 0
static char *VALUE = "1";
#else
static char *VALUE = "1113222113";
#endif

int64_t lookTell(char* in, int8_t repeats) {
    char* ret;
    char* copy = malloc(strlen(in) * sizeof(char));
    int64_t idx = 0;
    strcpy(copy, in);
    for (int8_t i = 0; i < repeats; i++) {
        int64_t s = 2*sizeof(char)*strlen(copy);
        ret = malloc(s);
        char c = copy[0];
        int8_t l = 1;
        for (int64_t j = 1; j < strlen(copy); j++) {
            if (c == copy[j]) {
                l++;
            } else {
                ret[idx++] = '0' + l;
                ret[idx++] = c;
                c = copy[j];
                l = 1;
            }
        }
        ret[idx++] = '0' + l;
        ret[idx++] = c;
        idx = 0;
        // printf("> %s\n", ret);
        copy = realloc(copy, strlen(ret)*sizeof(char));
        strcpy(copy, ret);
        free(ret);
    }
    int64_t length = strlen(copy);
    free(copy);
    return length;
}


void part1() {
    int64_t k = lookTell(VALUE, 40);
    printf("Part 1: %ld\n", k);
}

void part2() {
    int64_t k = lookTell(VALUE, 50);
    printf("Part 2: %ld\n", k);
}

int main(void) {
    part1();
    //part2();
    return 0;
}
