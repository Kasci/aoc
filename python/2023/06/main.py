#!/usr/bin/env python3

import sys
sys.path.append("../../")
sys.path.append("../")
import util as u

###############
debug = False
###############

file = "sample.txt" if debug else "input.txt"

def read_input():
    return u.read_lines(file)

def part1():
    x = [a.split(" ")[1:] for a in read_input()]
    A = [[int(b) for b in a if len(b)>0] for a in x]
    k = 1
    for j in range(len(A[0])):
        n = 0
        t = A[0][j]
        d = A[1][j]
        for i in range(t):
            if d < i*(t-i):
                n += 1
        k *= n
    print("Part 1:",k)

def part2():
    A = [int("".join(a.split(":")[1].split())) for a in read_input()]
    k = 0
    t = A[0]
    d = A[1]
    for i in range(t):
        if d < i*(t-i):
            k += 1
    print("Part 2:",k)

part1()
part2()
