#include "../../util.h"

#if 0
static char *FILE_NAME = "sample.txt";
#else
static char *FILE_NAME = "input.txt";
#endif


int8_t report(char a, char b) {
    size_t aa = a-'A';
    size_t bb = b-'X';
    if (aa==bb) return 3 + bb + 1;
    else if ((aa+1)%3 == bb) return 6 + bb + 1;
    else return 0 + bb + 1;
}

int8_t result(char a, char b) {
    size_t aa = a-'A';
    size_t bb = b-'X';
    int8_t ret = 3 * bb;
    if (aa == 0) {
        ret += bb == 0 ? 3 : bb == 1 ? 1 : 2;
    } else if (aa == 1) {
        ret += bb == 0 ? 1 : bb == 1 ? 2 : 3;
    } else {
        ret += bb == 0 ? 2 : bb == 1 ? 3 : 1;
    }
    return ret;
}

void part1() {
    ARR_STRING* in = readInput(FILE_NAME);
    int64_t k = 0;
    for (int64_t i = 0; i < in->length; i++) {
        k += report(in->strings[i][0],in->strings[i][2]);
    }
    printf("Part 1: %ld\n", k);
    freeArrString(in);
}

void part2() {
    ARR_STRING* in = readInput(FILE_NAME);
    int64_t k = 0;
    for (int64_t i = 0; i < in->length; i++) {
        k += result(in->strings[i][0],in->strings[i][2]);
    }
    printf("Part 2: %ld\n", k);
    freeArrString(in);
}

int main(void) {
    part1();
    part2();
    return 0;
}
