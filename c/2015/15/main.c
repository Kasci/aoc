#include "../../util.h"

#if 0
static char *FILE_NAME = "sample.txt";
#else
static char *FILE_NAME = "input.txt";
#endif

int64_t s(int8_t arr[][5], int64_t l, int8_t idx, int8_t coef[]) {
    int64_t ret = 0;
    for (int64_t i = 0; i < l; i++) {
        ret += arr[i][idx]*coef[i];
    }
    return ret > 0 ? ret : 0;
}

void part1() {
    ARR_MUL_STRING* in = readInputDelim(FILE_NAME, " ,");
    int8_t arr[4][5];
    for (int8_t i = 0; i < in->length; i++) {
        for (int8_t j = 0; j < 5; j++) {
            arr[i][j] = atoi(in->strings[i].strings[2+2*j]);
        }
    }

    uint64_t max = 0;
    for (int8_t a = 0; a < 100; a++) {
        for (int8_t b = 0; b < 100; b++) {
            for (int8_t c = 0; c < 100; c++) {
                for (int8_t d = 0; d < 100; d++) {
                    if (a+b+c+d != 100) continue;
                    int64_t val[4];
                    uint64_t tmp = 1;
                    int8_t coef[4] = {a,b,c,d};
                    for (int8_t i = 0; i < 4; i++) {
                        val[i] = s(arr, in->length, i, coef);
                        tmp *= val[i];
                    }
                    if (tmp > max) {
                        max = tmp;
                    }
                }
            }
        }
    }
    printf("Part 1: %ld\n", max);
    freeArrMulString(in);
}

void part2() {
    ARR_MUL_STRING* in = readInputDelim(FILE_NAME, " ,");
    int8_t arr[4][5];
    for (int8_t i = 0; i < in->length; i++) {
        for (int8_t j = 0; j < 5; j++) {
            arr[i][j] = atoi(in->strings[i].strings[2+2*j]);
        }
    }

    uint64_t max = 0;
    for (int8_t a = 0; a < 100; a++) {
        for (int8_t b = 0; b < 100; b++) {
            for (int8_t c = 0; c < 100; c++) {
                for (int8_t d = 0; d < 100; d++) {
                    if (a+b+c+d != 100) continue;
                    int8_t coef[4] = {a,b,c,d};
                    int64_t cal = s(arr, in->length, 4, coef);
                    if (cal != 500) continue;
                    int64_t val[4];
                    uint64_t tmp = 1;
                    for (int8_t i = 0; i < 4; i++) {
                        val[i] = s(arr, in->length, i, coef);
                        tmp *= val[i];
                    }
                    if (tmp > max) {
                        max = tmp;
                    }
                }
            }
        }
    }
    printf("Part 2: %ld\n", max);
    freeArrMulString(in);
}

int main(void) {
    part1();
    part2();
    return 0;
}
