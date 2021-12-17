#include "../../util.h"

#if 0 
static char *FILE_NAME = "sample.txt";
#else
static char *FILE_NAME = "input.txt";
#endif


void part1() {
    ARR_INTEGER* in = readIntInput(FILE_NAME);
    int16_t k = 0;
    for (int16_t i = 1; i < in->length; i++) {
        if (in->integers[i-1] < in->integers[i]) {
            k++;
        }
    }
    printf("Part 1: %d\n", k);
    freeArrInteger(in);
}

void part2() {
    ARR_INTEGER* in = readIntInput(FILE_NAME);
    int16_t k = 0;
    int16_t diffL = in->length - 2;
    int16_t* diff = malloc(diffL * sizeof(int16_t));
    int16_t* ins = in->integers;
    for (int16_t i = 0; i < in->length - 2; i++) {
        diff[i] = ins[i] + ins[i+1] + ins[i+2];
    }
    for (int16_t i = 1; i < diffL; i++) {
        if (diff[i-1] < diff[i]) {
            k++;
        }
    }
    printf("Part 2: %d\n", k);
    free(diff);
    freeArrInteger(in);
}

int main(void) {
    part1();
    part2();
    return 0;
}
