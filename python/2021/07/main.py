#!/usr/bin/env python3

import sys
sys.path.append("../../")
import util as u

###############
debug = False
###############

file = "sample.txt" if debug else "input.txt"

def read_input():
    return [int(x) for x in u.read_lines(file)[0].split(",")]

def part1():
    A = read_input()
    maxA = max(A)
    k = min([sum([abs(a-i) for a in A]) for i in range(maxA+1)])
    print("Part 1:",k)

def part2():
    A = read_input()
    maxA = max(A)
    s = lambda x: x*(x+1)//2
    k = min([sum([s(abs(a-i)) for a in A]) for i in range(maxA+1)])
    print("Part 2:",k)

part1()
part2()
