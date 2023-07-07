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
    k = [] 
    P = [[a[i] for a in A] for i in range(len(A[0]))]
    for p in P:
        n = [[chr(ord('a')+i), 0] for i in range(26)]
        for q in p:
            n[ord(q)-ord('a')][1] += 1
        n = sorted(n, key=lambda x: x[1], reverse=True)
        k += n[0][0]
    print("Part 1:","".join(k))

def part2():
    A = read_input()
    k = [] 
    P = [[a[i] for a in A] for i in range(len(A[0]))]
    for p in P:
        n = [[chr(ord('a')+i), 0] for i in range(26)]
        for q in p:
            n[ord(q)-ord('a')][1] += 1
        n = sorted([nn for nn in n if nn[1] > 0], key=lambda x: x[1])
        k += n[0][0]
    print("Part 2:","".join(k))

part1()
part2()
