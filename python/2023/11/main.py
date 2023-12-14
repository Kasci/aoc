#!/usr/bin/env python3

import sys
sys.path.append("../../")
sys.path.append("../")
import util as u
import math

###############
debug = False
###############

file = "sample.txt" if debug else "input.txt"

def read_input():
    return u.read_lines(file)

def expand(A):
    B = []
    for a in A:
        if all([x=="." for x in a]):
            B.append(a)
        B.append(a)
    C = []
    for i in range(len(B[0])):
        Bx = "".join([b[i] for b in B])
        if all([x=="." for x in Bx]):
            C.append(Bx)
        C.append(Bx)
    D = []
    for i in range(len(C[0])):
        D.append("".join([b[i] for b in C]))
    return D

def part1():
    A = expand(read_input())
    
    G = []
    for i,x in enumerate(A):
        for j,y in enumerate(x):
            if y == "#":
                G.append((i,j))
    
    k = 0
    for i,g in enumerate(G):
        for j,gg in enumerate(G):
            if i<j:
                k += abs(gg[0]-g[0]) + abs(gg[1]-g[1])

    print("Part 1:",k)

def get_empty(A):
    R = []
    for i,a in enumerate(A):
        if all([x=="." for x in a]):
            R.append(i)
    C = []
    for i in range(len(A)):
        Ax = "".join([a[i] for a in A])
        if all([x=="." for x in Ax]):
            C.append(i)
    return (R,C)

def part2():
    A = read_input()
    R,C = get_empty(A)

    G = []
    N = 1000000-1
    for i,x in enumerate(A):
        nR = sum([1 if i > r else 0 for r in R])
        for j,y in enumerate(x):
            nC = sum([1 if j > c else 0 for c in C])
            if y == "#":
                G.append((i+(nR*N),j+(nC*N)))
    
    k = 0
    for i,g in enumerate(G):
        for j,gg in enumerate(G):
            if i<j:
                k += abs(gg[0]-g[0]) + abs(gg[1]-g[1])
    print("Part 2:",k)

part1()
part2()
