#!/usr/bin/env python3

import sys
sys.path.append("../../")
import util as u

###############
debug = False
###############

file = "sample.txt" if debug else "input.txt"

def update(a, p):
    if a == ">":
        return [p[0]+1, p[1]]
    elif a == "<":
        return [p[0]-1, p[1]]
    elif a == "^":
        return [p[0], p[1]+1]
    elif a == "v":
        return [p[0], p[1]-1]
    else:
        pass

def read_input():
    return u.read_lines(file)

def part1():
    A = read_input()
    k = 0
    p = [0,0]
    L = []
    L.append(p)
    for a in A[0]:
        p = update(a, p)
        if p not in L: 
            L.append(p)
    print("Part 1:",len(L))

def part2():
    A = read_input()
    k = 0
    p = [0,0]
    pp = [0,0]
    L = []
    L.append(p)
    for i,a in enumerate(A[0]):
        if i % 2 == 0:
            p = update(a, p)
            if p not in L: 
                L.append(p)
        else:
            pp = update(a, pp)
            if pp not in L: 
                L.append(pp)
    print("Part 2:",len(L))
    

part1()
part2()
