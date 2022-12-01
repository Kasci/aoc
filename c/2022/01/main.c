#include "../../util.h"

#if 0
static char *FILE_NAME = "sample.txt";
#else
static char *FILE_NAME = "input.txt";
#endif


void part1() {
    ARR_STRING* in = readInput(FILE_NAME);
    int64_t k = 0;
    int64_t max = 0;
    for (int64_t i = 0; i < in->length; i++) {
        if (strlen(in->strings[i]) == 0) {
            if (max > k) k = max;
            max = 0;
        } else {
            max += atoi(in->strings[i]);
        }
    }
    printf("Part 1: %ld\n", k);
    freeArrString(in);
}

void part2() {
    ARR_STRING* in = readInput(FILE_NAME);
    int64_t k = 0;
    int64_t tmp = 0;
    int64_t max1 = 0, max2 = 0, max3 = 0;
    for (int64_t i = 0; i < in->length; i++) {
        if (strlen(in->strings[i]) == 0) {
            if (tmp > max1) {
                max3 = max2;
                max2 = max1;
                max1 = tmp;
            } else if (tmp > max2) {
                max3 = max2;
                max2 = tmp;
            } else if (tmp > max3) {
                max3 = tmp;
            }
            tmp = 0;
        } else {
            tmp += atoi(in->strings[i]);
        }
    }
    k = max1 + max2 + max3;
    printf("Part 2: %ld\n", k);
    freeArrString(in);
}

int main(void) {
    part1();
    part2();
    return 0;
}
