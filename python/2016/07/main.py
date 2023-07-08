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
    A = u.read_lines(file)
    return [[b for a in x.split("[") for b in a.split("]")] for x in A]

def match(x):
    for i in range(len(x)-3):
        q = x[i:i+4]
        if q[0]==q[3] and q[1]==q[2] and q[0]!=q[1]:
            return True
    return False

def net(x):
    k = []
    for i in range(len(x)-2):
        q = x[i:i+3]
        if q[0]==q[2] and q[0]!=q[1]:
            k.append(q)
    return k

def comp(a,b):
    return a[0] == b[1] and a[1] == b[0]

def cc(A,B):
    for a in A:
        for b in B:
            if comp(a,b): return True
    return False

def part1():
    A = read_input()
    k = 0
    for a in A:
        n = [match(a[i]) for i in range(len(a))]
        a = [x for i,x in enumerate(n) if i%2 == 0]
        b = [x for i,x in enumerate(n) if i%2 == 1]
        k += 1 if any(a) and not(any(b)) else 0
    print("Part 1:",k)

def part2():
    A = read_input()
    k = 0
    for a in A:
        n = [net(a[i]) for i in range(len(a))]
        a = [y for i,x in enumerate(n) if i%2 == 0 for y in x]
        b = [y for i,x in enumerate(n) if i%2 == 1 for y in x]
        k += 1 if cc(a,b) else 0
    print("Part 2:",k)

part1()
part2()
