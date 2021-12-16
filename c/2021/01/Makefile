CC = gcc
LPATH = -I ../.. -L ../..
LIBS = -lm ../../util.a
STANDARD = --std=c99

all: clean build

build:
	${CC} ${STANDARD} ${LPATH} main.c -o main.out ${LIBS} 

clean:
	rm *.out
