#!/usr/bin/env python3

import sys
sys.path.append("../../")
import util as u
from collections import Counter 
###############
debug = False
###############

file = "sample.txt" if debug else "input.txt"

def read_input():
    return [int(x) for x in u.read_lines(file)[0].split(",")]

def part1():
    A = read_input()
    for day in range(80):
        c = sum([1 if a == 0 else 0 for a in A])
        A = [7 if a == 0 else a for a in A] + [9 for i in range(c)]
        A = [a-1 for a in A]
    k = len(A)
    print("Part 1:",k)

def part2():
    A = read_input()
    c = Counter(A)
    for day in range(256):
        cc = Counter()
        for v in c:
            if v == 0:
                cc[6] += c[0]
                cc[8] += c[0]
                continue
            cc[v-1]+=c[v]
        c = cc
    k = sum(c.values())
    print("Part 2:",k)

part1()
part2()
