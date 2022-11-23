#include "../../util.h"

#if 0
static char *FILE_NAME = "sample.txt";
#else
static char *FILE_NAME = "input.txt";
#endif

char* subStr(char* str, char* dest, int16_t i) {
    dest[0] = str[i];
    dest[1] = str[i+1];
    dest[2] = '\0';
}

bool isNice1(char* str) {
    int a = 0;
    for (int16_t i = 0; i < strlen(str); i++) {
        if (str[i] == 'a' || str[i] == 'e' || str[i] == 'i' || str[i] == 'o' || str[i] == 'u') a++;
    }
    bool b = false;
    for (int16_t i = 0; i < strlen(str) - 1; i++) {
        b |= str[i] == str[i+1];
    }
    bool c = true;
    for (int16_t i = 0; i < strlen(str) - 1; i++) {
        char tmp[3] = "";
        subStr(str, tmp, i);
        c &= strcmp(tmp, "ab") && strcmp(tmp, "cd") && strcmp(tmp, "pq") && strcmp(tmp, "xy");
    }
    return a >= 3 && b && c;
}

bool isNice2(char* str) {
    bool a = false;
    for (int16_t i = 0; i < strlen(str) - 1; i++) {
        char tmp[3] = "";
        subStr(str, tmp, i);
        for (int16_t j = i+2; j < strlen(str) - 1; j++) {
            char tmp2[3] = "";
            subStr(str, tmp2, j);
            a |= !strcmp(tmp, tmp2); 
        }
    }
    bool b = false;
    for (int16_t i = 0; i < strlen(str) - 2; i++) {
        b |= str[i] == str[i+2];
    }
    return a && b;
}

void part1() {
    ARR_STRING* in = readInput(FILE_NAME);
    int64_t k = 0;
    for (int16_t i = 0; i < in->length; i++) {
        if (isNice1(in->strings[i])) k++;
    }
    printf("Part 1: %ld\n", k);
    freeArrString(in);
}

void part2() {
    ARR_STRING* in = readInput(FILE_NAME);
    int64_t k = 0;
    for (int16_t i = 0; i < in->length; i++) {
        if (isNice2(in->strings[i])) k++;
    }
    printf("Part 2: %ld\n", k);
    freeArrString(in);
}

int main(void) {
    part1();
    part2();
    return 0;
}
