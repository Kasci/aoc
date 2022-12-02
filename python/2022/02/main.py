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
    return u.read_match(file, "([ABC]) ([XYZ])")

def pts(b):
    return 3 if b=='Z' else 2 if b=='Y' else 1

def report(a,b):
    if (a=='A' and b=='X') or (a=='B' and b=='Y') or (a=='C' and b=='Z'):
        return 3 + pts(b)
    elif (a=='A' and b=='Y') or (a=='B' and b=='Z') or (a=='C' and b=='X'):
        return 6 + pts(b)
    else:
        return 0 + pts(b)

def result(a,b):
    ret = 6 if b=='Z' else 3 if b=='Y' else 0
    if (a=='A'):
        ret += 3 if b=='X' else 1 if b=='Y' else 2
    elif (a=='B'):
        ret += 1 if b=='X' else 2 if b=='Y' else 3
    else:
        ret += 2 if b=='X' else 3 if b=='Y' else 1
    return ret

def part1():
    A = read_input()
    k = sum([report(a,b) for a,b in A])
    print("Part 1:",k)

def part2():
    A = read_input()
    k = sum([result(a,b) for a,b in A])
    print("Part 2:",k)

part1()
part2()