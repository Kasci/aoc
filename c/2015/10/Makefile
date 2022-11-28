CC = gcc
LPATH = -I ../.. -L ../..
LIBS = -lm -pthread ../../util.a
STANDARD = --std=c99 

all:
	${CC} ${STANDARD} ${LPATH} main.c -o main.out ${LIBS} 

debug:
	${CC} -g ${STANDARD} ${LPATH} main.c -o main.out ${LIBS} 

clean:
	rm *.out
