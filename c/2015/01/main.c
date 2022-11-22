#include "../../util.h"

#if 0
static char *FILE_NAME = "sample.txt";
#else
static char *FILE_NAME = "input.txt";
#endif

void part1() {
    ARR_STRING* in = readInput(FILE_NAME);
    printf("%d\n",in->length);
    int64_t k = 0;
    char* s = in->strings[0];
    for (int32_t i = 0; i < strlen(s); i++) {
        if (s[i] == '(') k++; else k--;
    }
    printf("Part 1: %ld\n", k);
    freeArrString(in);
}

void part2() {
    ARR_STRING* in = readInput(FILE_NAME);
    int64_t k = 0;
    char* s = in->strings[0];
    int64_t t = 0;
    for (int32_t i = 0; i < strlen(s); i++) {
        if (s[i] == '(') t++; else t--;
        if (t == -1) {
            k = i + 1;
            break;
        }
    }
    printf("Part 2: %ld\n", k);
    freeArrString(in);
}

int main(void) {
    part1();
    part2();
    return 0;
}
