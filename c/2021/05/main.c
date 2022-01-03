#include "../../util.h"

#if 0
static char *FILE_NAME = "sample.txt";
#else
static char *FILE_NAME = "input.txt";
#endif

int16_t** getCoord(ARR_STRING* in) {
    int16_t** coord = malloc(in->length*sizeof(int16_t*));
    for (int i = 0; i < in->length; i++) {
        coord[i] = malloc(4*sizeof(int16_t));
        char* tmp;
        tmp = strtok(in->strings[i],", ->");
        int j = 0;
        while (tmp != NULL) {
            if (strlen(tmp) > 0) {
                coord[i][j++] = atoi(tmp);
            }
            tmp = strtok(NULL,", ->");
        }
    }
    return coord;
}

int16_t sign(int16_t x) {
    return x > 0 ? 1 : x < 0 ? -1 : 0;
}

void append(int64_t **map, int64_t* size, int64_t x, int64_t y) {
    for (int64_t i=0; i<(*size); i++) {
        if (map[i][0] == x && map[i][1] == y) {
            map[i][2] += 1;
            return;
        }
    }
    map[*size] = malloc(3*sizeof(int64_t));
    map[*size][0] = x;
    map[*size][1] = y;
    map[*size][2] = 1;
    (*size)++;
    return;
}

void printMap(int64_t **map, int64_t size) {
    for (int64_t i=0; i<size; i++) {
        printf("M %ld %ld %ld\n",map[i][0], map[i][1], map[i][2]);
    }
    printf("\n");
}

int64_t getCount(int16_t** coord, int64_t length, bool filter) {
    int64_t **map = malloc(500000*sizeof(int64_t*));
    int64_t size = 0;

    for (int64_t i = 0; i < length; i++) {
        if (filter && (coord[i][0] != coord[i][2] && coord[i][1] != coord[i][3])) continue;
        int64_t xD = coord[i][2]-coord[i][0];
        int64_t yD = coord[i][3]-coord[i][1];
        int64_t xS = sign(xD);
        int64_t yS = sign(yD);
        int64_t x,y;
        for (x=0,y=0; x!=xD || y!=yD; x+=xS,y+=yS) {
            append(map, &size, coord[i][0]+x, coord[i][1]+y);
        }
        append(map, &size, coord[i][0]+x, coord[i][1]+y);
    }
    
    int64_t count = 0;
    for (int64_t i = 0; i < size; i++) {
        if (map[i][2] > 1) count++;
    }
    for (int64_t i = 0; i<size; i++) {
        free(map[i]);
    }
    free(map);
    return count;
}

void part1() {
    ARR_STRING* in = readInput(FILE_NAME);
    int16_t** coord = getCoord(in);
    int64_t k = getCount(coord,in->length,true);
    printf("Part 1: %ld\n", k);
    for (int i = 0; i < in->length; i++) {
        free(coord[i]);
    }
    free(coord);
    freeArrString(in);
}

void part2() {
    ARR_STRING* in = readInput(FILE_NAME);
    int16_t** coord = getCoord(in);
    int64_t k = getCount(coord,in->length,false);
    printf("Part 2: %ld\n", k);
    for (int i = 0; i < in->length; i++) {
        free(coord[i]);
    }
    free(coord);
    freeArrString(in);
}

int main(void) {
    printf("This solution takes long time to execute, but only up to a minute.\n");
    part1();
    part2();
    return 0;
}
