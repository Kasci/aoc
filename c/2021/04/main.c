#include "../../util.h"

#if 0
static char *FILE_NAME = "sample.txt";
#else
static char *FILE_NAME = "input.txt";
#endif

typedef struct bingo {
    int16_t** bingo;
    bool** seen;
} BINGO;

BINGO* createBingo() {
    BINGO* bingo = malloc(sizeof(BINGO));
    bingo->bingo = malloc(5*sizeof(int16_t*));
    bingo->seen = malloc(5*sizeof(int8_t*));
    for (int i = 0; i < 5; i++) { 
    	bingo->bingo[i] = malloc(5*sizeof(int16_t));
        bingo->seen[i] = malloc(5*sizeof(int8_t));
	    for (int j = 0; j < 5; j++) {
            bingo->seen[i][j] = false;
        } 
    }
    return bingo;
}

void printBingo(BINGO* bingo) {
    for (int8_t i = 0; i < 5; i++) {
        for (int8_t j = 0; j < 5; j++) {
            printf("%2d%c\t", bingo->bingo[i][j], bingo->seen[i][j] > 0 ? '*' : ' ');
        }
        printf("\n");
    }
    printf("\n");
}

void freeBingo(BINGO* bingo) {
    for (int i = 0; i < 5; i++) {
    	free(bingo->bingo[i]);
    	free(bingo->seen[i]);
    }
    free(bingo->bingo);
    free(bingo->seen);
    free(bingo);
}

BINGO** initBingos(ARR_MUL_STRING* in, int64_t* q) {
    *q = (in->length-1)/6;
    BINGO** bs = malloc((*q)*sizeof(BINGO*));
    for (int64_t n = 0; n < *q; n++) {
        bs[n] = createBingo();
    	for (int64_t i = 0; i < 6; i++) {
	        int64_t line = i+n*6+1;
	        if (in->strings[line].length == 0) continue;
    	    for (int64_t j = 0; j < in->strings[line].length; j++) {
                //printf("%s\n",in->strings[line].strings[j]);
	            bs[n]->bingo[i-1][j] = atoi(in->strings[line].strings[j]);
 	        }
	    }
    }
    return bs;
}

int16_t* initNumbers(char* l, int64_t* index) {
    int16_t* numbers = malloc(200*sizeof(int16_t));
    char* tmp;
    tmp = strtok(l, ",");
    while (tmp != NULL) {
        numbers[(*index)++] = atoi(tmp);
        tmp = strtok(NULL, ",");
    }
    return numbers;
}

void pickNumber(BINGO* bingo, int16_t number) {
    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 5; j++) {
            if (bingo->bingo[i][j] == number)
                bingo->seen[i][j] = true;
        }
    }
}

bool isSolved(BINGO* bingo) {
    for (int i = 0; i < 5; i++) {
        bool hor = true, ver = true;
        for (int j = 0; j < 5; j++) {
            ver &= bingo->seen[i][j];
            hor &= bingo->seen[j][i];
        }
        if (hor || ver) return true;
    }
    return false;
}

void processBoards(BINGO** bs, int64_t q, int16_t* numbers, int64_t nL, int16_t* i, int16_t* n) { 
    for (*i = 0; *i < nL; (*i)++) {
        for (*n = 0; *n < q; (*n)++) {
            pickNumber(bs[*n], numbers[*i]);
            if (isSolved(bs[*n])) return;
        }
    }
}

void processBoards2(BINGO** bs, int64_t q, int16_t* numbers, int64_t nL, int16_t* i, int16_t* n) { 
    bool* solved = malloc(200*sizeof(bool));
    for (*i = 0; *i < nL; (*i)++) {
        for (*n = 0; *n < q; (*n)++) {
            pickNumber(bs[*n], numbers[*i]);
            if (isSolved(bs[*n]) && !solved[*n]) {
                solved[*n] = true;
                int8_t w;
                for (w = 0; w<nL; w++) {
                    if (!solved[w]) break;
                }
                if (w == q) return;
            }
        }
    }
}

int16_t get(BINGO* bingo) {
    int16_t sum = 0;
    for (int i=0; i<5; i++) {
        for (int j=0; j<5; j++) {
            if (!bingo->seen[i][j]) sum += bingo->bingo[i][j];
        }
    }
    return sum;
}

void part1() {
    ARR_MUL_STRING* in = readInputDelim(FILE_NAME, " ");
    char* l = in->strings[0].strings[0];
    //printf("%s\n",l);
    int64_t q = 0;
    BINGO** bs = initBingos(in, &q);
    int64_t nL = 0;
    int16_t* numbers = initNumbers(l, &nL);

    int16_t i,n;
    processBoards(bs,q,numbers,nL,&i,&n);

    int64_t k = numbers[i]*get(bs[n]);

    printf("Part 1: %ld\n", k);
    
    // FREE
    for (int64_t n = 0; n < q; n++) {
        freeBingo(bs[n]);
    }
    free(bs);
    free(numbers);
    freeArrMulString(in);
}

void part2() {
    ARR_MUL_STRING* in = readInputDelim(FILE_NAME, " ");
    char* l = in->strings[0].strings[0];

    int64_t q = 0;
    BINGO** bs = initBingos(in, &q);
    int64_t nL = 0;
    int16_t* numbers = initNumbers(l, &nL); 

    int16_t i,n;
    processBoards2(bs,q,numbers,nL,&i,&n);

    int64_t k = numbers[i]*get(bs[n]);

    printf("Part 2: %ld\n", k);
    
    // FREE
     for (int64_t n = 0; n < q; n++) {
        freeBingo(bs[n]);
    }
    free(bs);
    free(numbers);
    freeArrMulString(in);
}

int main(void) {
    part1();
    part2();
    return 0;
}
