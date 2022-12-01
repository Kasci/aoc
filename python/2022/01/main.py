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
    A = read_input()
    k = 0
    tmp = 0
    for a in A:
        if len(a) == 0:
            if tmp > k:
                k = tmp
            tmp = 0
        else:
            tmp += int(a)
    if tmp > k:
        k = tmp
    print("Part 1:",k)

def part2():
    A = read_input()
    k = 0
    tmp = 0
    n = []
    for a in A:
        if len(a) == 0:
            n.append(tmp)
            tmp = 0
        else:
            tmp += int(a)
    n.append(tmp)
    n = sorted(n)
    k = n[-1] + n[-2] + n[-3]
    print("Part 2:",k)

part1()
part2()
