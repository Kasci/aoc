#include "../../util.h"

#if 0
static char *FILE_NAME = "sample.txt";
#else
static char *FILE_NAME = "input.txt";
#endif

int64_t step(uint8_t deer[], int64_t time) {
    int64_t ret = 0;
    int64_t t = time;
    while (t > deer[1]+deer[2]) {
        ret += deer[0]*deer[1];
        t -= deer[1]+deer[2];
    }
    if (t >= deer[1]) {
        ret += deer[0]*deer[1];
    } else {
        ret += deer[0]*t;
    }
    return ret;
}

int64_t iter(uint8_t deer[][3], int16_t length, int16_t time) {
    int16_t l[length];
    for (int64_t i = 0; i < time; i++) {
        for (int16_t j = 0; j < length; j++) {
            l[j] = step(deer[j], i+1);
        }
    }
    uint64_t max = 0;
    for (int16_t j = 0; j < length; j++) {
        if (max < l[j]) {
            max = l[j];
        }
    }
    return max;
}

int64_t point(uint8_t deer[][3], int16_t length, int16_t time) {
    int64_t l[length];
    int64_t p[length];
    for (int16_t j = 0; j < length; j++) {
        p[j] = 0;
    }
    for (int64_t i = 0; i < time; i++) {
        for (int16_t j = 0; j < length; j++) {
            l[j] = step(deer[j], i+1);
        }
        uint64_t max = 0;
        for (int16_t j = 0; j < length; j++) {
            if (max < l[j]) {
                max = l[j];
            }
        }
        for (int16_t j = 0; j < length; j++) {
            if (l[j] == max) {
                p[j]++;
            }
        }
    }
    uint64_t max = 0;
    for (int16_t j = 0; j < length; j++) {
        if (max < p[j]) {
            max = p[j];
        }
    }
    return max;
}

void part1() {
    ARR_MUL_STRING* in = readInputDelim(FILE_NAME, " ");
    uint8_t deers[9][3];
    for (int8_t i = 0; i < in->length; i++) {
        deers[i][0] = atoi(in->strings[i].strings[3]);
        deers[i][1] = atoi(in->strings[i].strings[6]);
        deers[i][2] = atoi(in->strings[i].strings[13]);
    }
    int64_t k = iter(deers, in->length, 2503);
    printf("Part 1: %ld\n", k);
    freeArrMulString(in);
}

void part2() {
    ARR_MUL_STRING* in = readInputDelim(FILE_NAME, " ");
    uint8_t deers[9][3];
    for (int8_t i = 0; i < in->length; i++) {
        deers[i][0] = atoi(in->strings[i].strings[3]);
        deers[i][1] = atoi(in->strings[i].strings[6]);
        deers[i][2] = atoi(in->strings[i].strings[13]);
    }
    int64_t k = point(deers, in->length, 2503);
    printf("Part 2: %ld\n", k);
    freeArrMulString(in);
}

int main(void) {
    part1();
    part2();
    return 0;
}
