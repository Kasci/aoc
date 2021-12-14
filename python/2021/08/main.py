#!/usr/bin/env python3

import sys
sys.path.append("../../")
import util as u

###############
debug = False
###############

file = "sample.txt" if debug else "input.txt"

def read_input():
    return [[y.strip().split(" ") for y in x.split("|")] for x in u.read_lines(file)]

def part1():
    A = read_input()
    k = len([n for a in A for n in a[1] if len(n) in [2,3,4,7]])
    print("Part 1:",k)

def sor(N):
    return "".join(sorted(list(N)))

def part2():
    A = read_input()
    NN = 0 
    for a in A:
        d = {}
        a1 = sor([n for n in a[0] if len(n) == 2][0])
        a7 = sor([n for n in a[0] if len(n) == 3][0])
        a4 = sor([n for n in a[0] if len(n) == 4][0])
        a8 = sor([n for n in a[0] if len(n) == 7][0])
        d[a1] = 1
        d[a7] = 7
        d[a4] = 4
        d[a8] = 8
        n5 = [sor(n) for n in a[0] if len(n) == 5]
        i4 = "".join([x for x in list(a4) if x not in a1])
        a3 = [n for n in n5 if all([x in n for x in a1])][0]
        a5 = [n for n in n5 if all([x in n for x in i4])][0]
        a2 = [n for n in n5 if n != a3 and n != a5][0]
        d[a3] = 3
        d[a5] = 5
        d[a2] = 2
        n6 = [sor(n) for n in a[0] if len(n) == 6]
        a9 = [n for n in n6 if all([x in n for x in a4])][0]
        a0 = [n for n in n6 if n != a9 and all([x in n for x in a1])][0]
        a6 = [n for n in n6 if n != a9 and n != a0][0]
        d[a9] = 9
        d[a0] = 0
        d[a6] = 6
        N = 0
        for b in a[1]:
            N *= 10
            N += d[sor(b)]
        NN += N
    k = NN
    print("Part 2:",k)

part1()
part2()
