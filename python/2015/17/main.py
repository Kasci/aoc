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
    return [int(x) for x in u.read_lines(file)]

def fill(A, n):
    k = 0
    for i,a in enumerate(A):
        if n-a == 0:
            k += 1
        elif n-a > 0:
            k += fill(A[i+1:], n-a)
    return k

dp = [0]*20

def fill_depth(A, n, d):
    for i,a in enumerate(A):
        if n-a == 0:
            dp[d] += 1
        elif n-a > 0:
            fill_depth(A[i+1:], n-a, d+1) 

def part1():
    A = read_input()
    k = fill(A, 150)
    print("Part 1:",k)

def part2():
    A = read_input()
    fill_depth(A, 150, 0)
    k = 0
    while dp[k] == 0:
        k+=1
    print("Part 2:",dp[k])

part1()
part2()
