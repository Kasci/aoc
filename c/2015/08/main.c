#include "../../util.h"

#if 0
static char *FILE_NAME = "sample.txt";
#else
static char *FILE_NAME = "input.txt";
#endif

int16_t unescape(char* str) {
    int16_t index = 0;
    for (int16_t i = 1; i < strlen(str)-1; i++) {
        if (str[i] != '\\') {
            index++;
        } else {
            if (str[i+1] == '\\') {
                index++;
                i++;
            } else if (str[i+1] == '"') {
                index++;
                i++;
            } else {
                index++;
                i+=3;
            }
        }
    }
    return index;
}

int16_t escape(char* str) {
    int16_t index = 2;
    for (int16_t i = 0; i < strlen(str); i++) {
        if (str[i] == '"' || str[i] == '\\') index++;
        index++;
    }
    return index;
}

void part1() {
    ARR_STRING* in = readInput(FILE_NAME);
    int64_t k = 0;
    for (int16_t i = 0; i < in->length; i++) {
        k += strlen(in->strings[i]);
        k -= unescape(in->strings[i]);
    }
    freeArrString(in);
    printf("Part 1: %ld\n", k);
}

void part2() {
    ARR_STRING* in = readInput(FILE_NAME);
    int64_t k = 0;
    for (int16_t i = 0; i < in->length; i++) {
        k -= strlen(in->strings[i]);
        k += escape(in->strings[i]);
    }
    printf("Part 2: %ld\n", k);
    freeArrString(in);
}

int main(void) {
    part1();
    part2();
    return 0;
}
