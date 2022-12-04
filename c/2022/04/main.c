#include "../../util.h"

#if 0
static char *FILE_NAME = "sample.txt";
#else
static char *FILE_NAME = "input.txt";
#endif


void part1() {
    ARR_MUL_INTEGERS* in = readIntInputDelim(FILE_NAME,"-,");
    printf("%d\n",in->length);
    int64_t k = 0;
    for (int64_t i = 0; i < in->length; i++) {
        if ((in->integers[i].integers[0] <= in->integers[i].integers[2] && in->integers[i].integers[1] >= in->integers[i].integers[3]) ||
            (in->integers[i].integers[0] >= in->integers[i].integers[2] && in->integers[i].integers[1] <= in->integers[i].integers[3]))
            k++;
    }
    printf("Part 1: %ld\n", k);
    freeArrMulInteger(in);
}

void part2() {
    ARR_MUL_INTEGERS* in = readIntInputDelim(FILE_NAME,"-,");
    int64_t k = 0;    
    for (int64_t i = 0; i < in->length; i++) {
        if (in->integers[i].integers[1] >= in->integers[i].integers[2] && in->integers[i].integers[0] <= in->integers[i].integers[3])
            k++;
    }
    printf("Part 2: %ld\n", k);
    freeArrMulInteger(in);
}

int main(void) {
    part1();
    part2();
    return 0;
}
