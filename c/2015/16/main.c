#include "../../util.h"

#if 0
static char *FILE_NAME = "sample.txt";
#else
static char *FILE_NAME = "input.txt";
#endif

struct val {
    char name[15];
    int8_t val;
};

struct val AUNT[10] = {{.name = "children", .val = 3}, {.name="cats", .val=7}, {.name="samoyeds", .val=2}, {.name="pomeranians", .val=3}, {.name="akitas", .val=0}, {.name="vizslas", .val=0}, {.name="goldfish", .val=5}, {.name="trees", .val=3}, {.name="cars", .val=2}, {.name="perfumes", .val=1}};

bool t(struct val aunt) {
    for (int8_t i = 0; i < 10; i++) {
        if (!strcmp(aunt.name, AUNT[i].name)) {
            return aunt.val == AUNT[i].val;
        }
    }
    return false;
}

bool tt(struct val aunt) {
    for (int8_t i = 0; i < 10; i++) {
        if (!strcmp(aunt.name, AUNT[i].name)) {
            if (!strcmp(aunt.name, "cats") || !strcmp(aunt.name, "trees")) {
                return aunt.val > AUNT[i].val;
            } else if (!strcmp(aunt.name, "pomeranians") || !strcmp(aunt.name, "goldfish")) {
                return aunt.val < AUNT[i].val;
            } else {
                return aunt.val == AUNT[i].val;
            }
        }
    }
    return false;
}

void part1() {
    ARR_MUL_STRING* in = readInputDelim(FILE_NAME, " :,");
    int64_t k = 0;
    struct val aunt[500][3];
    for (int16_t i = 0; i < in->length; i++) {
        for (int16_t j = 0; j < 3; j++) {
            strcpy(aunt[i][j].name, in->strings[i].strings[2 + 2*j]);
            aunt[i][j].val = atoi(in->strings[i].strings[3 + 2*j]);
        }
        if (t(aunt[i][0]) && t(aunt[i][1]) && t(aunt[i][2])) {
            k = i+1;
            break;
        }
    }
    printf("Part 1: %ld\n", k);
    freeArrMulString(in);
}

void part2() {
    ARR_MUL_STRING* in = readInputDelim(FILE_NAME, " :,");
    int64_t k = 0;
    struct val aunt[500][3];
    for (int16_t i = 0; i < in->length; i++) {
        for (int16_t j = 0; j < 3; j++) {
            strcpy(aunt[i][j].name, in->strings[i].strings[2 + 2*j]);
            aunt[i][j].val = atoi(in->strings[i].strings[3 + 2*j]);
        }
        if (tt(aunt[i][0]) && tt(aunt[i][1]) && tt(aunt[i][2])) {
            k = i+1;
            break;
        }
    }
    printf("Part 2: %ld\n", k);
    freeArrMulString(in);
}

int main(void) {
    part1();
    part2();
    return 0;
}
