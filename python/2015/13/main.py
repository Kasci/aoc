#!/usr/bin/env python3

import sys
sys.path.append("../../")
sys.path.append("../")
import util as u

from operator import xor

###############
debug = False
###############

file = "sample.txt" if debug else "input.txt"

def read_input():
    return u.read_match(file, "(.*) would (.*) (.*) happiness units by sitting next to (.*).")

def paths(set, name, invalid, value):
    A = [a for a in set if a[0] == name and a[1] not in invalid]
    if len(A) == 0:
        x = [a for a in set if a[0] == name and a[1] == invalid[0]][0]
        return value + x[2]
    max = 0
    for a in A:
        k = paths(set, a[1], invalid+[name], value+a[2])
        if k > max:
            max = k
    return max

def part1():
    B = [(a[0], a[3], (1 if a[1] == "gain" else -1)*int(a[2])) if a[0] < a[3] else (a[3], a[0], (1 if a[1] == "gain" else -1)*int(a[2])) for a in read_input()]
    C = []
    names = []
    for b in B:
        C.append((b[0], b[1], sum([x[2] for x in B if x[0] == b[0] and x[1] == b[1]])))
        C.append((b[1], b[0], sum([x[2] for x in B if x[0] == b[0] and x[1] == b[1]])))
        names.append(b[0])
        names.append(b[1])
    names = set(names)
    C = set(C)
    # print(C)
    for n in names:
        k = paths(C, n, [], 0)
    print("Part 1:",k)

def part2():
    B = [(a[0], a[3], (1 if a[1] == "gain" else -1)*int(a[2])) if a[0] < a[3] else (a[3], a[0], (1 if a[1] == "gain" else -1)*int(a[2])) for a in read_input()]
    C = []
    names = []
    for b in B:
        C.append((b[0], b[1], sum([x[2] for x in B if x[0] == b[0] and x[1] == b[1]])))
        C.append((b[1], b[0], sum([x[2] for x in B if x[0] == b[0] and x[1] == b[1]])))
        names.append(b[0])
        names.append(b[1])
    for n in names:
        C.append(("Me",n,0))
        C.append((n,"Me",0))
    names.append("Me")
    names = set(names)
    C = set(C)
    # print(C)
    for n in names:
        k = paths(C, n, [], 0)
    print("Part 2:",k)

part1()
part2()
