#!/usr/bin/env python3

import sys
sys.path.append("../../")
import util as u

###############
debug = False
###############

file = "sample.txt" if debug else "input.txt"

def read_input():
    A = u.read_match(file,"(\d+),(\d+) -> (\d+),(\d+)")
    return [[int(x) for x in a] for a in A]

def dump(N):
    for n in N:
        for x in n:
            print("%3s" % x, end="")
        print()
    print()

def sign(k):
    return 0 if k == 0 else k//abs(k)

def write(a,N):
    x,y,xx,yy = a[0],a[1],a[2],a[3]
    dx, dy = sign(xx-x), sign(yy-y)
    while True:
        N[y][x] += 1
        if x == xx and y == yy:
            break
        x += dx
        y += dy
    return N

def part1():
    A = read_input()
    maxX = max([a[0] for a in A]+[a[2] for a in A])+1
    maxY = max([a[1] for a in A]+[a[3] for a in A])+1
    A = [a for a in A if a[0]==a[2] or a[1]==a[3]]
    N = [[0 for i in range(maxX)] for j in range(maxY)]
    for a in A:
        N = write(a,N)
    k = sum([1 if x > 1 else 0 for n in N for x in n])
    print("Part 1:",k)

def part2():
    A = read_input()
    maxX = max([a[0] for a in A]+[a[2] for a in A])+1
    maxY = max([a[1] for a in A]+[a[3] for a in A])+1
    N = [[0 for i in range(maxX)] for j in range(maxY)]
    for a in A:
        N = write(a,N)
    k = sum([1 if x > 1 else 0 for n in N for x in n])
    print("Part 2:",k)

part1()
part2()
