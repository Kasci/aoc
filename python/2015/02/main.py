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
    k = 0
    for a in A:
        b = [int(x) for x in a.split("x")]
        b.sort()
        k += 3*b[0]*b[1] + 2*(b[1]*b[2] + b[2]*b[0]) 
    print("Part 1:",k)

def part2():
    A = read_input()
    k = 0
    for a in A:
        b = [int(x) for x in a.split("x")]
        b.sort()
        k += 2*b[0] + 2*b[1] + b[0]*b[1]*b[2]
    print("Part 2:",k)

part1()
part2()
