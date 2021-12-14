#!/usr/bin/env python3

import sys
sys.path.append("../../")
import util as u

###############
debug = False
###############

file = "sample.txt" if debug else "input.txt"

def read_input():
    return [[int(x) for x in a] for a in u.read_lines(file)]

def flash(A):
    for i in range(10):
        for j in range(10):
            A[i][j] += 1
    k = 0
    while True:
        kk = 0
        for i,a in enumerate(A):
            for j,n in enumerate(a):
                if n == 10:
                    kk += 1
                    for y in range(-1,2):
                        for x in range(-1,2):
                            if i+y >= 0 and i+y < len(A) and j+x >= 0 and j+x < len(A[0]) and A[i+y][j+x] < 10:
                                A[i+y][j+x] += 1
                    A[i][j] = 11
        if kk == 0:
            break
        k += kk
    for i in range(10):
        for j in range(10):
            if A[i][j] == 11:
                A[i][j] = 0
    return k,A

def part1():
    A = read_input()
    k = 0
    for step in range(100):
        n, A = flash(A)
        k += n
    print("Part 1:",k)

def part2():
    A = read_input()
    k = 0
    step = 0
    while True:
        n, A = flash(A)
        step += 1
        if n == 100:
            k = step
            break

    print("Part 2:",k)

part1()
part2()
