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
    return u.read_match(file, "Card[ ]*(\d+): ([0-9 ]+) \| ([0-9 ]+)")

def part1():
    A = read_input()
    k = 0
    for a in A:
        w = [int(y) for y in a[1].split(" ") if len(y) > 0]
        d = [int(y) for y in a[2].split(" ") if len(y) > 0]
        n = len([x for x in w if x in d])
        if n > 0:
            k += pow(2, n-1)
    print("Part 1:",k)

def part2():
    A = read_input()
    k = 0
    N = [1 for i in range(len(A))]
    for i,a in enumerate(A):
        w = [int(y) for y in a[1].split(" ") if len(y) > 0]
        d = [int(y) for y in a[2].split(" ") if len(y) > 0]
        n = len([x for x in w if x in d])
        for j in range(n):
            N[i+j+1] += N[i]
    k = sum(N)
    print("Part 2:",k)

part1()
part2()
