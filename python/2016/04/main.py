#!/usr/bin/env python3

import sys
sys.path.append("../../")
sys.path.append("../")
import util as u

###############
debug =False 
###############

file = "sample.txt" if debug else "input.txt"

def read_input():
    return u.read_match(file,"([a-z\-]+)(\d+)\[(\w+)\]")

def part1():
    A = read_input()
    k = 0
    for a in A:
        X = [0 for _ in range(ord('a'),ord('z')+1)]
        p = a[0].replace("-","")
        for i in p:
            X[ord(i)-ord('a')] += 1
        n = sorted([(chr(ord('a')+i),a) for i,a in enumerate(X)], key=lambda x: x[1], reverse=True)
        v = "".join([q[0] for q in n[0:5]])
        if v == a[2]:
            k += int(a[1])
    print("Part 1:",k)

def part2():
    A = read_input()
    k = 0
    for a in A:
        n = int(a[1]) % 26
        g = "".join([" " if p == "-" else chr((ord(p) - ord('a') + n)%26 + ord('a')) for p in a[0]])
        if "north" in g:
            k = int(a[1])
    print("Part 2:",k)


part1()
part2()
