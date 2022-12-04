#include "../../util.h"

#if 0
static char *FILE_NAME = "sample.txt";
#else
static char *FILE_NAME = "input.txt";
#endif

int64_t fill(ARR_INTEGER* arr, int16_t start, int64_t n) {
    int64_t k = 0;
    for (int16_t i = start; i < arr->length; i++) {
        if (n - arr->integers[i] == 0) {
            k += 1;
        } else if (n - arr->integers[i] > 0) {
            k += fill(arr, i+1, n - arr->integers[i]);
        }
    }
    return k;
}

int16_t dp[20];

void fill_depth(ARR_INTEGER* arr, int16_t start, int64_t n, int16_t d) {
    for (int16_t i = start; i < arr->length; i++) {
        if (n - arr->integers[i] == 0) {
            dp[d] += 1;
        } else if (n - arr->integers[i] > 0) {
            fill_depth(arr, i+1, n - arr->integers[i], d+1);
        }
    }
}

#define N 150

void part1() {
    ARR_INTEGER* in = readIntInput(FILE_NAME);
    int64_t k = fill(in, 0, N);
    printf("Part 1: %ld\n", k);
    freeArrInteger(in);
}

void part2() {
    ARR_INTEGER* in = readIntInput(FILE_NAME);
    fill_depth(in, 0, N, 0);
    int64_t k = 0;
    while (dp[k] == 0) k++;
    printf("Part 2: %ld\n", dp[k]);
    freeArrInteger(in);
}

int main(void) {
    part1();
    part2();
    return 0;
}
