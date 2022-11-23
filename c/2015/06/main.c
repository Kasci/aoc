#include "../../util.h"

#if 0
static char *FILE_NAME = "sample.txt";
#else
static char *FILE_NAME = "input.txt";
#endif

#define L 1000

void parse(char *A, int16_t *a) {
    int16_t i = strcspn(A, ",");
    char p[50] = "";
    strncpy(p, A, i);
    a[0] = atoi(p);
    strcpy(p, A+i+1);
    a[1] = atoi(p);
}

void getAll(ARR_STRING strings, size_t* type, int16_t a[], int16_t b[]) {
    char A[10];
    char B[10];
    memset(A, 0, 10);
    memset(B, 0, 10);
    if (strings.length == 4) {
        *type = 2;
        strcpy(A, strings.strings[1]);
        strcpy(B, strings.strings[3]);
    } else {
        strcpy(A, strings.strings[2]);
        strcpy(B, strings.strings[4]);
        if (!strcmp(strings.strings[1], "on")) {
            *type = 1;
        } else {
            *type = 0;
        }
    }
    
    parse(A, a);
    parse(B, b);
}

void update1(ARR_STRING strings, int8_t arr[L][L]) {
    size_t type;
    int16_t a[2], b[2];
    
    getAll(strings, &type, a, b);

    for (int16_t i = a[0]; i <= b[0]; i++) {
        for (int16_t j = a[1]; j <= b[1]; j++) {
            arr[i][j] = (type == 2 ? !arr[i][j] : type);
        }
    }
}

void update2(ARR_STRING strings, int8_t arr[L][L]) {
    size_t type;
    int16_t a[2], b[2];
    
    getAll(strings, &type, a, b);

    for (int16_t i = a[0]; i <= b[0]; i++) {
        for (int16_t j = a[1]; j <= b[1]; j++) {
            arr[i][j] += (type == 0 ? -1 : type);
            if (arr[i][j] < 0) arr[i][j] = 0;
        }
    }
}

void part1() {
    ARR_MUL_STRING* in = readInputDelim(FILE_NAME, " ");
    int8_t arr[L][L];
    for (int16_t i = 0;  i < L; i++) {
        for (int16_t j = 0; j < L; j++) {
            arr[i][j] = 0;
        }
    }
    int64_t k = 0;
    for (int16_t i = 0;  i < in->length; i++) {
        update1(in->strings[i], arr);  
    }
    for (int16_t i = 0; i < L; i++) {
        for (int16_t j = 0; j < L; j++) {
            k += arr[i][j];
        }
    }
    printf("Part 1: %ld\n", k);
    freeArrMulString(in);
}

void part2() {
    ARR_MUL_STRING* in = readInputDelim(FILE_NAME, " ");
    int8_t arr[L][L];
    for (int16_t i = 0;  i < L; i++) {
        for (int16_t j = 0; j < L; j++) {
            arr[i][j] = 0;
        }
    }
    int64_t k = 0;
    for (int16_t i = 0;  i < in->length; i++) {
        update2(in->strings[i], arr);  
    }
    for (int16_t i = 0; i < L; i++) {
        for (int16_t j = 0; j < L; j++) {
            k += arr[i][j];
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
