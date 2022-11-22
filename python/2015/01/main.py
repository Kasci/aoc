#!/usr/bin/env python3

import sys
sys.path.append("../../")
import util as u

###############
debug = False
###############

file = "sample.txt" if debug else "input.txt"

def read_input():
    return u.read_lines(file)

def part1():
    A = read_input()
    k = sum([1 if a == '(' else -1 for a in A[0]])
    print("Part 1:",k)

def part2():
    A = read_input()
    k = 0
    s = 0
    for i,n in enumerate([1 if a == '(' else -1 for a in A[0]]):
        s += n
        if s == -1:
            k = i
            break
    print("Part 2:",k)

part1()
part2()
