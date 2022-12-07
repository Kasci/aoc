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

def read_input():
    X = u.read_lines(file)
    return [x.split(" => ") for x in X[:-2]], X[-1]

def part1():
    A, mol = read_input()
    B = []
    for a in A:
        n = ["","",mol]
        p = ""
        while a[0] in n[2]:  
            p += n[0] + n[1]
            n = n[2].partition(a[0])
            B.append("".join([p,n[0],a[1],n[2]]))
    B = set(B)
    k = len(B)
    print("Part 1:",k)

K = 0

def repl(t, AA):
    global K
    while True:
        changed = False
        for a in AA:
            x = t.replace(a[1], a[0], 1)
            while x != t:
                print(">",t, x)
                K += 1
                t = x
                changed = True
        if not changed:
            break
    return t

def part2():
    K = "NOT IMPLEMENTED YET";
    print("Part 2:", K)  

part1()
part2()
