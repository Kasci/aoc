#!/usr/bin/env python3

import sys
sys.path.append("../../")
import util as u

###############
debug = False
###############

file = "sample.txt" if debug else "input.txt"

def read_input():
    return [int(x) for x in u.read_match(file,"target area: x=(-?\d+)\.\.(-?\d+), y=(-?\d+)\.\.(-?\d+)")[0]]

def simulate(i,j,A):
    step = 0
    x,y = 0,0
    dx,dy = i,j
    maxY = 0
    while True:
        x += dx
        y += dy
        if abs(dx) > 0:
            dx -= 1 if x > 0 else -1 if x < 0 else 0
        dy -= 1
        if y > maxY:
            maxY = y
        if min([A[0],A[1]]) <= x <= max([A[0],A[1]]) and min([A[2],A[3]]) <= y <= max([A[2],A[3]]):
            return maxY
        if x > max([A[0],A[1]]) or y < min([A[2],A[3]]):
            return -1
        step += 1

def part1():
    A = read_input()
    k = 0
    for i in range(500):
        for j in range(500):
            kk = simulate(i,j,A)
            if kk > k:
                k = kk
    print("Part 1:",k)

def part2():
    A = read_input()
    k = 0
    for i in range(max(A[0],A[1])+1):
        for j in range(min(A[2], A[3]),1000):
            k += 1 if simulate(i,j,A) != -1 else 0
    print("Part 2:",k)

part1()
part2()
