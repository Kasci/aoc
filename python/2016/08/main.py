#!/usr/bin/env python3

import sys
sys.path.append("../../")
sys.path.append("../")
import util as u
import re

###############
debug = False
###############

file = "sample.txt" if debug else "input.txt"
N = (7,3) if debug else (50,6)

def read_input():
    return u.read_lines(file)

def printQ(Q):
    for q in Q:
        print("".join(['.' if i == 0 else '#' for i in q]))
    print("-"*10)

def evaluate(a,Q):
    rect = re.match("rect (.+)x(.+)", a)
    row = re.match("rotate row y=(.+) by (.+)", a)
    col = re.match("rotate column x=(.+) by (.+)", a)
    if rect != None:
        c = int(rect.group(1))
        r = int(rect.group(2))
        return [[1 if i < c and j < r else Q[j][i] for i in range(N[0])] for j in range(N[1])]
    if row != None:
        r = int(row.group(1))
        o = int(row.group(2))
        return [[Q[j][(N[0]+i-o)%N[0]] for i in range(N[0])] if j == r else Q[j] for j in range(N[1])]
    if col != None:
        c = int(col.group(1))
        o = int(col.group(2))
        return [[Q[(N[1]+j-o)%N[1]][i] if c == i else Q[j][i] for i in range(N[0])] for j in range(N[1])]

def part1():
    A = read_input()
    Q = [[0 for _ in range(N[0])] for _ in range(N[1])]
    for a in A:
        Q = evaluate(a,Q)
    print("Part 1:",sum([i for q in Q for i in q]))

def part2():
    A = read_input()
    Q = [[0 for _ in range(N[0])] for _ in range(N[1])]
    for a in A:
        Q = evaluate(a,Q)
    print("Part 2:")
    printQ(Q)


part1()
part2()
