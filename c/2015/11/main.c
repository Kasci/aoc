#include "../../util.h"

#if 0
static char *VALUE = "abcdefgh";
#else
static char *VALUE = "cqjxjnds";
#endif

bool check(char* v) {
    bool a = false;
    for (int8_t i = 0; i < strlen(v)-2; i++) {
        a |= v[i]+1 == v[i+1] && v[i+1]+1 == v[i+2];
    }
    bool b = true;
    for (int8_t i = 0; i < strlen(v); i++) {
        b &= v[i] != 'i' && v[i] != 'l' && v[i] != 'o';
    }
    char c;
    int8_t idx = 0;
    for (int8_t i = 0; i < strlen(v)-1; i++) {
        if (v[i] == v[i+1]) {
            if (idx == 0) {
                c = v[i];
                idx++;
            } else if (idx == 1 && c != v[i]) {
                idx++;
            }
        } 
    }
    return a && b && idx>1;
}

char* increment(char* v) {
    bool carry = true;
    for (int8_t i = strlen(v)-1; i >= 0; i--) {
        if (carry) {
            if (v[i] == 'z') {
                v[i] = 'a';
            } else {
                v[i] = v[i]+1;
                carry = false;
            }
        } else break;
    }
    // printf(">%s\n",v);
    return v;
}
 
char* next(char* v) {
    while (!check(v)) {
        v = increment(v);
    }
    return v;
}


void part1() {
    char c[9];
    strcpy(c,VALUE);
    char* cc = next(c);
    printf("Part 1: %s\n", cc);
}

void part2() {
    char c[9];
    strcpy(c,VALUE);
    char* cc = next(c);
    cc = increment(cc);
    cc = next(cc);
    printf("Part 2: %s\n", cc);
}

int main(void) {
    part1();
    part2();
    return 0;
}
