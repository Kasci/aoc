#include "../../util.h"

#if 0
static char *FILE_NAME = "sample.txt";
#else
static char *FILE_NAME = "input.txt";
#endif

void update(char c, int32_t* x, int32_t* y) {
    if (c == '>') {
        *x += 1;
    } else if (c == '<') {
        *x -= 1;
    } else if (c == '^') {
        *y += 1;
    } else if (c == 'v') {
        *y -= 1;
    }
}

bool inStack(POINT* pts, int16_t size, POINT p) {
    for (int16_t i = 0; i < size; i++) {
        POINT q = pts[i];
        if (comparePoints(p, q)) return true;
    }
    return false;
}

void part1() {
    ARR_STRING* in = readInput(FILE_NAME);
    printf("%d\n",in->length);
    char* s = in->strings[0];
    int64_t k = 0;
    POINT* pts = (POINT*) malloc(1024 * sizeof(POINT));
    int32_t x = 0, y = 0;
    int16_t index = 0;
    int16_t size = 1024;
    for (int32_t i = 0; i < strlen(s)+1; i++) {
        POINT p = {.x=x, .y=y, .z=0};
        if (index + 1 >= size) {
            size += 1024;
            pts = realloc(pts, size * sizeof(POINT));
        } 
        if (!inStack(pts, index, p)) {
            pts[index++] = p;
        }
        update(s[i], &x, &y);
    }
    k = index;
    printf("Part 1: %ld\n", k);
    free(pts);
    freeArrString(in);
}

void part2() {
    ARR_STRING* in = readInput(FILE_NAME);
    char* s = in->strings[0];
    int64_t k = 0;
    POINT* pts = (POINT*) malloc(1024 * sizeof(POINT));
    int32_t x = 0, y = 0, xx = 0, yy = 0;
    int16_t index = 0;
    int16_t size = 1024;
    for (int32_t i = 0; i < strlen(s)+1; i+=2) {
        POINT p1 = {.x=x, .y=y, .z=0};
        POINT p2 = {.x=xx, .y=yy, .z=0};
        
        if (index + 2 >= size) {
            size += 1024;
            pts = realloc(pts, size * sizeof(POINT));
        } 
        if (!inStack(pts, index, p1)) {
            pts[index++] = p1;
        }
        if (!inStack(pts, index, p2)) {
            pts[index++] = p2;
        }
        update(s[i], &x, &y);
        update(s[i+1], &xx, &yy);
    }
    k = index;
    printf("Part 2: %ld\n", k);
    free(pts);
    freeArrString(in);
}

int main(void) {
    part1();
    part2();
    return 0;
}
