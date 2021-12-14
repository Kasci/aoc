#!/usr/bin/env python3

import sys
sys.path.append("../../")
import util as u

###############
debug = False
###############

file = "sample.txt" if debug else "input.txt"

def read_input():
    A = []
    B = []
    C = u.read_lines(file)
    for a in C:
        if a == "":
            continue
        if ',' in a:
            A.append([int(x) for x in a.split(',')])
        else:
            B.append(a[11:].split('='))
    return A,B

def printN(N):
    for n in N:
        for nn in n:
            print("#" if nn == 1 else " ",end="")
        print()
    print()

def rot(p):
    return [[p[i][j] for i in range(len(p))] for j in range(len(p[0]))]

def split(Q, i):
    if i <= len(Q)//2:
        Qa, Qb = Q[:i], Q[i+1:]
        Qa.reverse()
        for i,a in enumerate(Qa):
            for j,b in enumerate(a):
                Qb[i][j] |= b
        Qb.reverse()
        return Qb
    else:
        Qa, Qb = Q[:i], Q[i+1:]
        Qa.reverse()
        for i,a in enumerate(Qb):
            for j,b in enumerate(a):
                Qa[i][j] |= b
        Qa.reverse()
        return Qa


def part1():
    A,B = read_input()
    maxX = max([a[0] for a in A])+1
    maxY = max([a[1] for a in A])+1

    N = []
    for y in range(maxY):
        n = []
        for x in range(maxX):
            n.append(0)
        N.append(n)
    
    for a in A:
        N[a[1]][a[0]] = 1

    for b in B:
        if b[0] == "y":
            N = split(N, int(b[1]))
        else:
            N = rot(N)
            N = split(N, int(b[1]))
            N = rot(N)
        break
    k = sum([x for n in N for x in n])
    print("Part 1:",k)

def part2():
    A,B = read_input()
    maxX = max([a[0] for a in A])+1
    maxY = max([a[1] for a in A])+1

    N = []
    for y in range(maxY):
        n = []
        for x in range(maxX):
            n.append(0)
        N.append(n)
    
    for a in A:
        N[a[1]][a[0]] = 1
    
    for b in B:
        if b[0] == "y":
            N = split(N, int(b[1]))
        else:
            N = rot(N)
            N = split(N, int(b[1]))
            N = rot(N)
    print("Part 2:")
    printN(N)

part1()
part2()

