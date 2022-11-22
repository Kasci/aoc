#include "../../util.h"

// library used from here: https://github.com/Zunawe/md5-c
#include "md5.h"

#if 0
static char *INPUT = "abcdef";
#else
static char *INPUT = "bgvyzdsv";
#endif

char* hash(char* str) {
    char* c = malloc(33);
    uint8_t* res = md5String(str);
    for (int8_t i=0; i<16; i++) {
        char s[2] = "";
        sprintf(s, "%02x", *res);
        strcpy(c+2*i, s);
        res += 1;
    }
    return c;
}

void part1() {
    int64_t k = 0;
    char t[20];
    while (true) {
        sprintf(t, "%s%d", INPUT, k);
        char* c = hash(t);
        char l[6] = "00000";
        if (!strncmp(l, c, 5)) break;
        k++;
    }
    printf("Part 1: %ld\n", k);
}

void part2() {
    int64_t k = 0;
    char t[20];
    while (true) {
        sprintf(t, "%s%d", INPUT, k);
        char* c = hash(t);
        char l[7] = "000000";
        if (!strncmp(l, c, 6)) break;
        k++;
    }
    printf("Part 2: %ld\n", k);
}

int main(void) {
    part1();
    part2();
    return 0;
}
