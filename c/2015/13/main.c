#include "../../util.h"

#if 0
static char *FILE_NAME = "sample.txt";
#else
static char *FILE_NAME = "input.txt";
#endif

typedef struct leaf {
    char a[10];
    char b[10];
    int16_t val;
} LEAF;

bool compare(LEAF a, LEAF b) {
    return !strcmp(a.a, b.a) && !strcmp(a.b, b.b);
}

bool cross_compare(LEAF a, LEAF b) {
    return !strcmp(a.a, b.b) && !strcmp(a.b, b.a);
}

bool in(char* a, char arr[][10], int16_t depth) {
    for (int16_t i = 0; i < depth; i++) {
        if (!strcmp(a, arr[i])) return true;
    }
    return false;
}

int64_t paths(LEAF leaf[], int64_t length, char* name, char invalid[][10], int8_t depth, int64_t value) {
    int64_t filtered_length = 0;
    LEAF l[10];
    for (int16_t i = 0; i < length; i++) {
        if (!strcmp(leaf[i].a, name) && !in(leaf[i].b, invalid, depth)) {
            l[filtered_length++] = leaf[i];
        }
    }
    if (filtered_length == 0) {
        for (int16_t i = 0; i < length; i++) {
            if (!strcmp(leaf[i].a, name) && !strcmp(leaf[i].b, invalid[0])) {
                return value + leaf[i].val;
            }
        }
    }
    int64_t max = 0;
    strcpy(invalid[depth], name);
    for (int16_t i = 0; i < filtered_length; i++) {
        int64_t k = paths(leaf, length, l[i].b, invalid, depth+1, value+l[i].val);
        if (k > max) {
            max = k;
        }
    } 
    return max;
}

void part1() {
    ARR_MUL_STRING* in = readInputDelim(FILE_NAME, " .");
    LEAF leaf[in->length];
    for (int64_t i = 0; i < in->length; i++) {
        strcpy(leaf[i].a, in->strings[i].strings[0]);
        strcpy(leaf[i].b, in->strings[i].strings[10]);
        if (!strcmp(in->strings[i].strings[2], "gain")) {
            leaf[i].val = atoi(in->strings[i].strings[3]);
        } else {
            leaf[i].val = -1 * atoi(in->strings[i].strings[3]);
        }
    }
    LEAF leaves[in->length];
    for (int64_t i = 0; i < in->length; i++) {
        strcpy(leaves[i].a, leaf[i].a);
        strcpy(leaves[i].b, leaf[i].b);
        leaves[i].val = leaf[i].val;
        for (int64_t j = 0; j < in->length; j++) {
            if (cross_compare(leaf[i], leaf[j])) {
                leaves[i].val += leaf[j].val;
            }
        }
    }
    char invalid[10][10] = {"","","","","","","","","",""};
    int64_t k = paths(leaves, in->length, "Alice", invalid, 0, 0);
    printf("Part 1: %ld\n", k);
    freeArrMulString(in);
}

void part2() {
    ARR_MUL_STRING* in = readInputDelim(FILE_NAME, " .");
    LEAF leaf[in->length];
    char names[10][10] = {"Alice"};
    int8_t count = 1;
    for (int64_t i = 0; i < in->length; i++) {
        strcpy(leaf[i].a, in->strings[i].strings[0]);
        strcpy(leaf[i].b, in->strings[i].strings[10]);
        if (!strcmp(leaf[i].a, "Alice")) {
            strcpy(names[count], leaf[i].b);
            count++;
        }
        if (!strcmp(in->strings[i].strings[2], "gain")) {
            leaf[i].val = atoi(in->strings[i].strings[3]);
        } else {
            leaf[i].val = -1 * atoi(in->strings[i].strings[3]);
        }
    }
    LEAF leaves[in->length + 2*count];
    for (int64_t i = 0; i < in->length; i++) {
        strcpy(leaves[i].a, leaf[i].a);
        strcpy(leaves[i].b, leaf[i].b);
        leaves[i].val = leaf[i].val;
        for (int64_t j = 0; j < in->length; j++) {
            if (cross_compare(leaf[i], leaf[j])) {
                leaves[i].val += leaf[j].val;
            }
        }
    }
    for (int64_t i = 0; i < count; i++) {
        strcpy(leaves[in->length + 2*i].a, "Me");
        strcpy(leaves[in->length + 2*i].b, names[i]);
        leaves[in->length + 2*i].val = 0;
        strcpy(leaves[in->length + 2*i + 1].a, names[i]);
        strcpy(leaves[in->length + 2*i + 1].b, "Me");
        leaves[in->length + 2*i + 1].val = 0;
    }
    char invalid[10][10] = {"","","","","","","","","",""};
    int64_t k = paths(leaves, (in->length) + 2*count, "Alice", invalid, 0, 0);
    printf("Part 2: %ld\n", k);
    freeArrMulString(in);
}

int main(void) {
    part1();
    part2();
    return 0;
}
