#!/usr/bin/env python3

import sys
sys.path.append("../../")
sys.path.append("../")
import util as u

###############
debug = False
###############

file = "sample.txt" if debug else "input.txt"

N = 0

def read_input():
    global N
    x = [[1 if x == '#' else 0 for x in a] for a in u.read_lines(file)]
    N = len(x)
    return x

def val(A, i, j):
    k = 0
    v = A[i][j]
    ys = i-1 if i-1 >= 0 else 0
    ye = i+2 if i+2 < N else N
    xs = j-1 if j-1 >= 0 else 0
    xe = j+2 if j+2 < N else N
    for y in range(ys, ye):
        for x in range(xs, xe):
            if x == j and y == i:
                continue
            k += A[y][x]
    if v == 0 and k == 3:
        return 1
    if v == 1 and (k == 2 or k == 3):
        return 1
    return 0      

def life(A):
    B = []
    for i in range(len(A)):
        b = []
        for j in range(len(A[0])):
            b.append(val(A, i, j))
        B.append(b)
    return B

def part1():
    A = read_input()
    for i in range(100):
        A = life(A)
    k = sum([x for a in A for x in a])
    print("Part 1:",k)

def stuck(A):
    A[0][0] = 1
    A[0][N-1] = 1
    A[N-1][0] = 1
    A[N-1][N-1] = 1
    return A

def part2():
    A = read_input()
    for i in range(100):
        A = stuck(A)
        A = life(A)
    A = stuck(A)
    k = sum([x for a in A for x in a])
    print("Part 2:",k)

part1()
part2()
