#!/usr/bin/env python3

import sys
sys.path.append("../../")
import util as u

###############
debug = False
###############

file = "sample.txt" if debug else "input.txt"

def read_input():
    return [[int(y) for y in list(x)] for x in u.read_lines(file)]

def is_low(x, y, maxX, maxY, A):
    a = A[y][x]
    up = A[y-1][x] if y-1 >= 0    else 99
    dn = A[y+1][x] if y+1 <  maxY else 99
    lf = A[y][x-1] if x-1 >= 0    else 99
    rg = A[y][x+1] if x+1 <  maxX else 99
    return up > a and dn > a and lf > a and rg > a

def part1():
    A = read_input()
    maxY = len(A)
    maxX = len(A[0])
    N = []
    for y in range(maxY):
        for x in range(maxX):
            if is_low(x,y,maxX,maxY,A):
                N.append(A[y][x])
    k = sum(N)+len(N)
    print("Part 1:",k)

def part2():
    A = read_input()
    maxY = len(A)
    maxX = len(A[0])
    N = []
    for y in range(maxY):
        for x in range(maxX):
            if is_low(x,y,maxX,maxY,A):
                N.append((x,y))
    B = [[[aa, False] for aa in a] for a in A]
    out = []
    for n in N:
        r = 0 
        q = [n]
        while len(q) > 0:
            x,y = q.pop()
            if B[y][x][1]:
                continue
            up = B[y-1][x][0] if y-1 >= 0    and not B[y-1][x][1] else 9
            dn = B[y+1][x][0] if y+1 <  maxY and not B[y+1][x][1] else 9
            lf = B[y][x-1][0] if x-1 >= 0    and not B[y][x-1][1] else 9
            rg = B[y][x+1][0] if x+1 <  maxX and not B[y][x+1][1] else 9
            if up < 9:
                q.append((x,y-1))
            if dn < 9:
                q.append((x,y+1))
            if lf < 9:
                q.append((x-1,y))
            if rg < 9:
                q.append((x+1,y))
            r += 1
            B[y][x][1] = True
        out.append(r)
    p = [x for i,x in enumerate(sorted(out, reverse=True)) if i < 3]
    k = p[0]*p[1]*p[2] 
    print("Part 2:",k)

part1()
part2()
