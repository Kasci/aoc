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
    ip = 0
    ic = 0
    x = 1
    k = 0
    is_add = False
    while True:
        ic += 1
        if ic == 20 or ic == 60 or ic == 100 or ic == 140 or ic == 180 or ic == 220:
            k += x * ic
        if A[ip] == "noop":
            ip += 1
        elif A[ip].startswith("addx"):
            if not is_add:
                is_add = True
            else:
                is_add = False
                p = A[ip].split(" ")[1]
                x += int(p)
                ip += 1
        if ip >= len(A):
            ip = 0
        if ic == 220:
            break
    print("Part 1:",k)

def part2():
    A = read_input()
    ip = 0
    ic = 0
    x = 1
    k = 0
    is_add = False
    R = ["","","","","",""]
    while True:
        R[ic//40] += "#" if ic%40 in [x-1,x,x+1] else "."
        ic += 1
        if A[ip] == "noop":
            ip += 1
        elif A[ip].startswith("addx"):
            if not is_add:
                is_add = True
            else:
                is_add = False
                p = A[ip].split(" ")[1]
                x += int(p)
                ip += 1
        if ip >= len(A):
            ip = 0
        if ic == 240:
            break
    print("Part 2:")
    for r in R:
        print(r)

part1()
part2()
