#include "../../util.h"

#if 0
static char *FILE_NAME = "sample.txt";
#else
static char *FILE_NAME = "input.txt";
#endif

int16_t N = 0;

int8_t** create() {
    int8_t** a = (int8_t**) malloc(N * sizeof(int8_t*));
    for (int8_t i = 0; i < N; i++) {
        a[i] = (int8_t*) malloc(N * sizeof(int8_t));
    }
    return a;
}

void freee(int8_t** a) {
    for (int8_t i = 0; i < N; i++) {
        free(a[i]);
    }
    free(a);
}

int8_t val(int8_t** A, int8_t i, int8_t j) {
    int8_t k = 0;
    int8_t v = A[i][j];
    int8_t ys = i-1 >= 0 ? i-1 : 0;
    int8_t ye = i+2 < N ? i+2 : N;
    int8_t xs = j-1 >= 0 ? j-1 : 0;
    int8_t xe = j+2 < N ? j+2 : N;
    for (int8_t y = ys; y < ye; y++) {
        for (int8_t x = xs; x < xe; x++) {
            if (x == j && y == i) continue;
            k += A[y][x];
        }
    }
    if (v == 0 && k == 3) return 1;
    if (v == 1 && (k == 2 || k == 3)) return 1;
    return 0;
}

int8_t** stuck(int8_t** A) {
    A[0][0] = 1;
    A[0][N-1] = 1;
    A[N-1][0] = 1;
    A[N-1][N-1] = 1;
    return A;
}

int8_t** life(int8_t** A) {
    int8_t** B = create();
    for (int8_t i = 0; i < N; i++) {
        for (int8_t j = 0; j < N; j++) {
            B[i][j] = val(A, i, j);
        }
    }
    freee(A);
    return B;
}

void part1() {
    ARR_STRING* in = readInput(FILE_NAME);
    N = in->length;
    int8_t** A = create();
    for (int8_t i = 0; i < N; i++) {
        for (int8_t j = 0; j < N; j++) {
            A[i][j] = in->strings[i][j] == '#' ? 1 : 0;
        }
    }
    for (int16_t i = 0; i < 100; i++) {
        A = life(A);
    }
    int64_t k = 0;
    for (int8_t i = 0; i < N; i++) {
        for (int8_t j = 0; j < N; j++) {
            k += A[i][j];
        }
    }
    printf("Part 1: %ld\n", k);
    freee(A);
    freeArrString(in);
}

void pr(int8_t** a) {
    for (int8_t i = 0; i < N; i++) {
        for (int8_t j = 0; j < N; j++) {
            printf("%c", a[i][j] == 1 ? '#' : ' ');
        }
        printf("\n");
    }
    printf("-----\n");
}

void part2() {
    ARR_STRING* in = readInput(FILE_NAME);
    N = in->length;
    int8_t** A = create();
    for (int8_t i = 0; i < N; i++) {
        for (int8_t j = 0; j < N; j++) {
            A[i][j] = in->strings[i][j] == '#' ? 1 : 0;
        }
    }
    for (int16_t i = 0; i < 100; i++) {
        A = stuck(A);
        // pr(A);
        A = life(A);
    }
    A = stuck(A);
    // pr(A);
    int64_t k = 0;
    for (int8_t i = 0; i < N; i++) {
        for (int8_t j = 0; j < N; j++) {
            k += A[i][j];
        }
    }
    printf("Part 2: %ld\n", k);
    freee(A);
    freeArrString(in);
}

int main(void) {
    part1();
    part2();
    return 0;
}
