#include "../../util.h"

#if 0
static char *FILE_NAME = "sample.txt";
#else
static char *FILE_NAME = "input.txt";
#endif

int64_t val(char i) {
    if (i >= 'a' && i <= 'z') return i-'a'+1;
    if (i >= 'A' && i <= 'Z') return i-'A'+27;
}

int64_t line(char* in) {
    int32_t l = strlen(in)/2;
    char a[l+1];
    char b[l+1];
    strncpy(a, in, l);
    a[l] = '\0';
    strncpy(b, in+l, l);
    b[l] = '\0';
    for (int16_t i = 0; i < l; i++) {
        for (int16_t j = 0; j < l; j++) {
            if (a[i] == b[j]) return val(a[i]);
        }
    }
}

int64_t tripple(char* a, char* b, char* c) {
    char x[100];
    int16_t idx = 0;
    for (int16_t i = 0; i < strlen(a); i++) {
        for (int16_t j = 0; j < strlen(b); j++) {
            if (a[i] == b[j]) x[idx++] = a[i];
        }
    }
    x[idx] = '\0';
    for (int16_t i = 0; i < strlen(x); i++) {
        for (int16_t j = 0; j < strlen(c); j++) {
            if (x[i] == c[j]) return val(x[i]);
        }
    }
}


void part1() {
    ARR_STRING* in = readInput(FILE_NAME);
    printf("%d\n",in->length);
    int64_t k = 0;
    for (int64_t i = 0; i < in->length; i++) {
        k += line(in->strings[i]);
    }
    printf("Part 1: %ld\n", k);
    freeArrString(in);
}

void part2() {
    ARR_STRING* in = readInput(FILE_NAME);
    int64_t k = 0;
    for (int64_t i = 0; i < in->length/3; i++) {
        k += tripple(in->strings[3*i],in->strings[3*i+1],in->strings[3*i+2]);
    }
    printf("Part 2: %ld\n", k);
    freeArrString(in);
}

int main(void) {
    part1();
    part2();
    return 0;
}
