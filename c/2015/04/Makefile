CC = gcc
LPATH = -I ../.. -L ../..
LIBS = -lm ../../util.a md5.c
STANDARD = --std=c99

all:
	${CC} ${STANDARD} ${LPATH} main.c -o main.out ${LIBS} 

clean:
	rm *.out
