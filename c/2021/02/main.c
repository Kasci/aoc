#include "../../util.h"

#if 0
static char *FILE_NAME = "sample.txt";
#else
static char *FILE_NAME = "input.txt";
#endif


void part1() {
    ARR_MUL_STRING* in = readInputDelim(FILE_NAME, " ");
    int64_t k = 0;
    int64_t hor = 0, ver = 0;
    for (int16_t i = 0; i < in->length; i++) {
        char* cmd = in->strings[i].strings[0];
        int val = atoi(in->strings[i].strings[1]);
        if (!strcmp(cmd,"forward")) {
            hor += val;
        } else if (!strcmp(cmd,"up")) {
            ver -= val;
        } else if (!strcmp(cmd,"down")) {
            ver += val;
        }
    }
    k = hor*ver;
    printf("Part 1: %ld\n", k);
    freeArrMulString(in);
}

void part2() {
    ARR_MUL_STRING* in = readInputDelim(FILE_NAME, " ");
    int64_t k = 0;
    int64_t aim = 0, hor = 0, ver = 0;
    for (int16_t i = 0; i < in->length; i++) {
        char* cmd = in->strings[i].strings[0];
        int val = atoi(in->strings[i].strings[1]);
        if (!strcmp(cmd,"forward")) {
            hor += val;
            ver += val*aim;
        } else if (!strcmp(cmd,"up")) {
            aim -= val;
        } else if (!strcmp(cmd,"down")) {
            aim += val;
        }
    }
    k = hor*ver;
    printf("Part 2: %ld\n", k);
    freeArrMulString(in);
}

int main(void) {
    part1();
    part2();
    return 0;
}
