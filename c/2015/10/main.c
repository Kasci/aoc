#include "../../util.h"

#include <sys/types.h>
#include <pthread.h>

#if 0
static char *VALUE = "1";
#else
static char *VALUE = "1113222113";
#endif

struct step_args {
    char* in; 
    int64_t start; 
    int64_t end;
};

void* step(void * args) {
    struct step_args *a = (struct step_args *) args;
    char* ret = malloc(1000000 * sizeof(char));
    if (a->start == a->end) {
        ret[0] = '\0';
        pthread_exit(ret);
    }
    int64_t idx = 0;
    char c = a->in[a->start];
    int8_t l = 1;
    for (int64_t j = a->start+1; j < a->end; j++) {
        if (c == a->in[j]) {
            l++;
        } else {
            ret[idx++] = '0' + l;
            ret[idx++] = c;
            c = a->in[j];
            l = 1;
        }
    }
    ret[idx++] = '0' + l;
    ret[idx++] = c;
    ret[idx++] = '\0';
    pthread_exit(ret);
}

#define DIV 500000

int64_t lookTell(char* in, int8_t repeats) {
    char* ret = malloc(4000000 * sizeof(char));
    char* copy = malloc(4000000 * sizeof(char));
    int64_t idx = 0;
    strcpy(copy, in);
    for (int8_t i = 0; i < repeats; i++) {
        if (strlen(copy) > DIV) {
            char* tmp;
            int8_t threads = strlen(copy) / DIV;
            pthread_t tid[threads+1];
            struct step_args args[threads+1];
            int64_t startIdx = 0;
            for (int8_t n = 0; n < threads+1; n++) {
                int64_t endIdx = DIV * (n+1);
                if (endIdx > strlen(copy)) {
                    endIdx = strlen(copy);
                } else {
                    while (endIdx+1 <= strlen(copy) && copy[endIdx-1] == copy[endIdx]) {
                        endIdx++;
                    }
                }
                // printf("* %c %c\n", copy[endIdx], copy[endIdx+1]);
                args[n].in = copy;
                args[n].start = startIdx;
                args[n].end = endIdx;
                startIdx = endIdx;
                pthread_create(&tid[n], NULL, step, &args[n]);
            }
            int64_t retIdx = 0;
            for (int8_t n = 0; n < threads+1; n++) {
                void* retVal;
                pthread_join(tid[n], &retVal);
                char* r = (char*)(off_t)retVal;
                strcpy(ret + retIdx, r);
                retIdx += strlen(r);
                free(r);
            }
        } else {
            int64_t idx = 0;
            char c = copy[0];
            int8_t l = 1;
            for (int64_t j = 1; j < strlen(copy); j++) {
                if (c == copy[j]) {
                    l++;
                } else {
                    ret[idx++] = '0' + l;
                    ret[idx++] = c;
                    c = copy[j];
                    l = 1;
                }
            }
            ret[idx++] = '0' + l;
            ret[idx++] = c;
        }
        idx = 0;
        strcpy(copy, ret);
        // printf("%s\n",copy);
    }
    int64_t length = strlen(copy);
    free(ret);
    free(copy);
    return length;
}


void part1() {
    int64_t k = lookTell(VALUE, 40);
    printf("Part 1: %ld\n", k);
}

void part2() {
    int64_t k = lookTell(VALUE, 50);
    printf("Part 2: %ld\n", k);
}

int main(void) {
    part1();
    part2();
    return 0;
}
