#include "../../util.h"

#if 1
static char *FILE_NAME = "sample.txt";
#else
static char *FILE_NAME = "input.txt";
#endif


void part1() {
    ARR_STRING* in = readInput(FILE_NAME);
    printf("%d\n",in->length);
    int64_t k = 0;
    printf("Part 1: %ld\n", k);
    freeArrString(in);
}

void part2() {
    assert(0);
    ARR_STRING* in = readInput(FILE_NAME);
    printf("Hello World\n");
    int64_t k = 0;
    printf("Part 2: %ld\n", k);
    freeArrString(in);
}

int main(void) {
    part1();
    //part2();
    return 0;
}
