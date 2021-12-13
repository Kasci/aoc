#!/usr/bin/env python3

import sys
sys.path.append("../../")
import util as u

###############
debug = False
###############

file = "sample.txt" if debug else "input.txt"

A = []

def read_input():
    return u.read_match(file, "([a-z]+) ([0-9]+)")

def part1():
    A = read_input()
    x,y = 0,0
    for a in A:
        m,n = a[0], int(a[1])
        if m == 'forward':
            x+=n
        elif m == 'down':
            y+=n
        elif m == 'up':
            y-=n
    print("Part 1",x*y)

def part2():
    A = read_input()
    x,y,aim = 0,0,0
    for a in A:
        m,n = a[0], int(a[1])
        if m == 'forward':
            x+=n
            y+=aim*n
        elif m == 'down':
            aim+=n
        elif m == 'up':
            aim-=n
    print("Part 1",x*y)

part1()
part2()
