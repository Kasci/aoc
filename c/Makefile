CC=gcc

all: clean build

build:
	${CC} -o util.o -c util.c
	ar -cvq util.a util.o

clean:
	rm *.a *.o
