#include "../../util.h"

#if 0
static char *FILE_NAME = "sample.txt";
#else
static char *FILE_NAME = "input.txt";
#endif


void part1() {
    ARR_MUL_INTEGERS* in = readIntInputDelim(FILE_NAME, "x");
    int64_t k = 0;
    for (int32_t i = 0; i<in->length; i++) {
        int16_t* s = in->integers[i].integers;
        int16_t a = s[0]*s[1];
        int16_t b = s[1]*s[2];
        int16_t c = s[2]*s[0];
        int16_t w = a<b? (a<c? a : (b<c ? b : c)) : b<c ? b : (a<c ? a : c);
        k += 2*(a + b + c) + w;
    }
    printf("Part 1: %ld\n", k);
    freeArrMulInteger(in);
}

void part2() {
    ARR_MUL_INTEGERS* in = readIntInputDelim(FILE_NAME, "x");
    int64_t k = 0;
    for (int32_t i = 0; i<in->length; i++) {
        int16_t* s = in->integers[i].integers;
        int16_t a = s[0]+s[1];
        int16_t b = s[1]+s[2];
        int16_t c = s[2]+s[0];
        int16_t w = a<b? (a<c? a : (b<c ? b : c)) : b<c ? b : (a<c ? a : c);
        k += s[0]*s[1]*s[2] + 2*w;
    }
    printf("Part 2: %ld\n", k);
    freeArrMulInteger(in);
}

int main(void) {
    part1();
    part2();
    return 0;
}
