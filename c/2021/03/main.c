#include "../../util.h"

#if 0
static char *FILE_NAME = "sample.txt";
#else
static char *FILE_NAME = "input.txt";
#endif


void part1() {
    ARR_STRING* in = readInput(FILE_NAME);
    int64_t k = 0, l = 0;
    for (int16_t i=0; i<strlen(in->strings[0]); i++) {
	int64_t ones = 0;
    	for (int16_t j=0; j<in->length; j++) {
	    if (in->strings[j][i] == '1') ones++;
	}
	k = k << 1 | (ones > in->length/2 ? 1 : 0);
	l = l << 1 | (ones <= in->length/2 ? 1 : 0);
    }
    printf("Part 1: %ld\n", k*l);
    freeArrString(in);
}

int p(ARR_STRING* in, int8_t* good, char c, char d) {
    for (int16_t i=0; i<strlen(in->strings[0]); i++) {
	int64_t ones = 0;
	int64_t size = 0;
    	for (int16_t j=0; j<in->length; j++) {
	    if (good[j] == 0) continue;
	    size++;
	    if (in->strings[j][i] == '1') ones++;
	}
	if (size == 1) break;
	char q = ones >= size/2.0f ? c : d;
    	for (int16_t j=0; j<in->length; j++) {
	    if (in->strings[j][i] != q) good[j] = 0;
	}
    }
    char *kk = malloc(100);
    for (int64_t n = 0; n < in->length; n++) {
	if (good[n] > 0) {
	    kk = strcpy(kk, in->strings[n]);
	    break;
	}
    }
    int64_t k = 0;
    for (int64_t i = 0; i < strlen(kk); i++) {
    	k = k << 1 | (kk[i] == '1' ? 1 : 0);
    }
    free(kk);
    return k;
}

void part2() {
    ARR_STRING* in = readInput(FILE_NAME);
    int64_t k = 0, l = 0;
    int8_t* good = malloc(sizeof(int8_t)*in->length);
    memset(good, 1, in->length);
    k = p(in, good, '1', '0');
    memset(good, 1, in->length); 
    l = p(in, good, '0', '1');
    printf("Part 2: %ld\n", k*l);
    free(good);
    freeArrString(in);
}

int main(void) {
    part1();
    part2();
    return 0;
}
