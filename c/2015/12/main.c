#include "../../util.h"

#if 0
static char *FILE_NAME = "sample.txt";
#else
static char *FILE_NAME = "input.txt";
#endif

void replace1(char* in) {
    char allowed[12] = "0123456789-";
    for (int64_t i = 0; i < strlen(in); i++) {
        if (strchr(allowed, in[i]) == NULL) {
            in[i] = ' ';
        }
    }
}

void replace2(char* in) {
    char allowed[20] = "0123456789-{}[]red";
    for (int64_t i = 0; i < strlen(in); i++) {
        if (strchr(allowed, in[i]) == NULL) {
            in[i] = ' ';
        }
    }
}

char* clean(char* in) {
    char* out = malloc(strlen(in) * sizeof(char));
    char nums[12] = "0123456789-";
    char brackets[4] = "[]{}";
    bool spaced = false;
    int64_t idx = 0;
    for (int64_t i = 0; i < strlen(in); i++) {
        if (strchr(nums, in[i]) != NULL) {
            out[idx++] = in[i];
            spaced = false;
        } else if (strchr(brackets, in[i])) {
            out[idx++] = ' ';
            out[idx++] = in[i];
            out[idx++] = ' ';
            spaced = true;
        } else if (in[i] == 'r' && in[i+1] == 'e' && in[i+2] == 'd') {
            out[idx++] = 'X';
            spaced = false;
            i += 2;
        } else if (in[i] == ' ' && !spaced) {
            out[idx++] = ' ';
            spaced = true;
        } 
    }
    out[idx] = '\0';
    return out;
}

void part1() {
    ARR_STRING* in = readInput(FILE_NAME);
    replace1(in->strings[0]);
    int64_t k = 0;
    char* pch = strtok(in->strings[0], " ");
    while (pch != NULL){
        k += atoi(pch);
        pch = strtok (NULL, " ");
    }
    printf("Part 1: %ld\n", k);
    freeArrString(in);
}

void part2() {
    ARR_STRING* in = readInput(FILE_NAME);
    replace2(in->strings[0]);
    char *cleaned = clean(in->strings[0]);
    
    int64_t partial[10000];
    bool isRed[10000];
    int64_t idx = 0;
    int64_t tmp = 0;
    bool tmpRed = false;
    char* pch = strtok(cleaned, " ");
    while (pch != NULL){
        if (!strcmp(pch, "{") || !strcmp(pch, "[")) {
            partial[idx] = tmp;
            isRed[idx] = tmpRed;
            idx++;
            tmp = 0;
            tmpRed = false;
        } else if (!strcmp(pch, "}")) {
            idx--;
            if (tmpRed) {
                tmp = partial[idx];
            } else {
                tmp += partial[idx];
            }
            tmpRed = isRed[idx];
        } else if (!strcmp(pch, "]")) {
            idx--;
            tmp += partial[idx];
            tmpRed = isRed[idx];
        } else if (!strcmp(pch, "X")) {
            tmpRed = true;
        } else {
            tmp += atoi(pch);
        }
        pch = strtok (NULL, " ");
    }
    int64_t k = tmp;
    printf("Part 2: %ld\n", k);
    free(cleaned);
    freeArrString(in);
}

int main(void) {
    part1();
    part2();
    return 0;
}
