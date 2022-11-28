#!/usr/bin/env python3

import sys
sys.path.append("../../")
sys.path.append("../")
import util as u

###############
debug = False
###############

file = "sample.txt" if debug else "input.txt"

def check(n):
    a = False
    for i in range(len(n)-2):
        a |= ord(n[i])+1 == ord(n[i+1]) and ord(n[i+1])+1 == ord(n[i+2])
    b = not ('i' in n or 'l' in n or 'o' in n)
    c = []
    for i in range(len(n)-1):
        if n[i] == n[i+1]:
            c.append(n[i])
    return a and b and len(set(c)) == 2

def increment(n):
    m = []
    over = True
    for i in range(len(n)-1, -1, -1):
        if over:
            if n[i] == 'z':
                m.append('a')
            else:
                m.append(chr(ord(n[i])+1))
                over = False
        else:
            m.append(n[i])
    m.reverse()
    n = "".join(m)
    return n

def next(n):
    while not check(n):
        n = increment(n)
    return n

def read_input():
    return "abcdefgh" if debug else "cqjxjnds"

def part1():
    A = read_input()
    k = next(A)
    print("Part 1:",k)

def part2():
    A = read_input()
    k = increment(next(A))
    k = next(k)
    print("Part 2:",k)

part1()
part2()
