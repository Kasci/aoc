#!/usr/bin/env python3

import sys
sys.path.append("../../")
import util as u

###############
debug = False
###############

file = "sample.txt" if debug else "input.txt"

def execute(L, n):
    command = n[0]
    a,b = int(n[1]), int(n[2])
    aa,bb = int(n[3]), int(n[4])
    if command == "turn on":
        for i in range(a,aa+1):
            L[i][b:bb+1] = [True for q in range(bb-b+1)]
    elif command == "toggle":
        for i in range(a,aa+1):
            for j in range(b,bb+1):
                L[i][j] = not L[i][j]
    elif command == "turn off":
        for i in range(a,aa+1):
            L[i][b:bb+1] = [False for q in range(bb-b+1)]

def execute2(L, n):
    command = n[0]
    a,b = int(n[1]), int(n[2])
    aa,bb = int(n[3]), int(n[4])
    if command == "turn on":
        for i in range(a,aa+1):
            for j in range(b,bb+1):
                L[i][j] = L[i][j] + 1
    elif command == "toggle":
        for i in range(a,aa+1):
            for j in range(b,bb+1):
                L[i][j] = L[i][j] + 2
    elif command == "turn off":
        for i in range(a,aa+1):
            for j in range(b,bb+1):
                L[i][j] = L[i][j] - 1 if L[i][j] > 0 else 0

def read_input():
    return u.read_match(file, "([a-z ]+) (\d+),(\d+) through (\d+),(\d+)")

def part1():
    A = read_input()
    L = [[False for i in range(1000)] for j in range(1000)]
    [execute(L, i) for i in A]
    k = sum([item for l in L for item in l])
    print("Part 1:",k) 

def part2():
    A = read_input()
    L = [[0 for i in range(1000)] for j in range(1000)]
    [execute2(L, i) for i in A]
    k = sum([item for l in L for item in l])
    print("Part 2:",k)

part1()
part2()
