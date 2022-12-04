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
    return [(int(x[0]), int(x[1]), int(x[2]), int(x[3]), int(x[4])) for x in u.read_match(file,".* (-?[0-9]+).* (-?[0-9]+).* (-?[0-9]+).* (-?[0-9]+).* (-?[0-9]+)")]

def mul(arr):
    ret = 1
    for a in arr:
        ret *= a
    return ret

def s(A, idx, n):
    ret = 0
    for i,x in enumerate(A):
        t = x[idx]*n[i]
        ret += t
    return ret if ret > 0 else 0

def part1():
    A = read_input()
    max = 0
    for a in range(100):
        for b in range(100):
            for c in range(100):
                for d in range(100):
                    if a+b+c+d != 100:
                        continue
                    g = [s(A, i, [a, b, c, d]) for i in range(4)]
                    x = mul(g)
                    if x > max:
                        max = x
    print("Part 1:",max)

def part2():
    A = read_input()
    max = 0
    for a in range(100):
        for b in range(100):
            for c in range(100):
                for d in range(100):
                    if a+b+c+d != 100:
                        continue
                    cal = s(A, 4, [a,b,c,d])
                    if cal != 500:
                        continue
                    g = [s(A, i, [a, b, c, d]) for i in range(4)]
                    x = mul(g)
                    if x > max:
                        max = x
    print("Part 2:",max)

    

part1()
part2()
