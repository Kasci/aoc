#!/usr/bin/env python3

import sys
sys.path.append("../../")
sys.path.append("../")
import util as u
import math

###############
debug = False
###############

file = "sample.txt" if debug else "input.txt"

def read_input():
    return u.read_lines(file)


def part1():
    A = read_input()
    p = A[0]
    L = dict([(x[0:3],(x[7:10], x[12:15]))for x in A[2:]])
    k = 0
    l = L["AAA"]
    while True:
        n = p[k%len(p)]
        x = l[0 if n == "L" else 1]
        l = L[x]
        k+=1
        if x == "ZZZ":
            break
    print("Part 1:",k)

def part2():
    A = read_input()
    k = 0
    p = A[0]
    L = dict([(x[0:3],(x[7:10], x[12:15]))for x in A[2:]])
    ln = [x for x in L if x.endswith("A")]
    steps = []
    for il in ln:
        first = False
        one = 0
        two = 0
        l = L[il]
        while True:
            n = p[two%len(p)]
            xn = l[0 if n == "L" else 1]
            l = L[xn]
            if not first:
                one+=1
            two+=1
            if xn.endswith("Z"):
                if first:
                    break
                else:
                    first = True
        steps.append((one, two))
    k = math.lcm(*[x[1]-x[0] for x in steps])
    print("Part 2:",k)

part1()
part2()
