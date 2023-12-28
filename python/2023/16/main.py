#!/usr/bin/env python3

import sys
sys.path.append("../../")
sys.path.append("../")
import util as u
from enum import Enum

###############
debug = False
###############

file = "sample.txt" if debug else "input.txt"

def read_input():
    return u.read_lines(file)

class Dir(Enum):
    LEFT = 0 
    RIGHT = 1
    UP = 2
    DOWN = 3

W, H = 0, 0

def update(x,y,d,A):
    if d is Dir.LEFT:
        x -= 1
    if d is Dir.RIGHT:
        x += 1
    if d is Dir.UP:
        y -= 1
    if d is Dir.DOWN:
        y += 1
    if (x < 0) or (x >= W) or (y < 0) or (y >= H):
        return []
    n = A[y][x]
    # print(">",n)
    if n == ".": return [(x,y,d)]
    elif n == "|": return [(x,y,d)] if d in [Dir.UP, Dir.DOWN] else [(x,y,Dir.UP),(x,y,Dir.DOWN)]
    elif n == "-": return [(x,y,d)] if d in [Dir.LEFT, Dir.RIGHT] else [(x,y,Dir.LEFT),(x,y,Dir.RIGHT)]
    elif n == "/": 
            if d is Dir.UP: return [(x,y,Dir.RIGHT)]
            elif d is Dir.DOWN: return [(x,y,Dir.LEFT)]
            elif d is Dir.LEFT: return [(x,y,Dir.DOWN)]
            elif d is Dir.RIGHT: return [(x,y,Dir.UP)]
            else: raise Exception("UNKOWN DIR")
    elif n == "\\":
            if d is Dir.UP: return [(x,y,Dir.LEFT)]
            elif d is Dir.DOWN: return [(x,y,Dir.RIGHT)]
            elif d is Dir.LEFT: return [(x,y,Dir.UP)]
            elif d is Dir.RIGHT: return [(x,y,Dir.DOWN)]
            else: raise Exception("UNKOWN DIR")
    else:
        raise Exception("UNKONWN TILE")
    raise Exception("Unreachable")

def printB(B):
    for b in B:
        print("".join(["X" if len(p) > 0 else "." for p in b]))

def run(X, A):
    B = []
    k = 0
    for a in A:
        B.append([[] for _ in range(len(a))])
    while len(X) > 0:
        i = X.pop(0)
        p = B[i[1]][i[0]]
        if i[2] in p:
             continue
        else:
            p.append(i[2])
        N = update(*i, A)
        X.extend(N)
    for b in B:
        for p in b:
            if len(p) > 0:
                k += 1 
    return k

def part1():
    global W,H
    A = read_input()
    H = len(A)
    W = len(A[0])
    X = update(*(-1,0,Dir.RIGHT), A)
    k = run(X,A)
    print("Part 1:",k)

def part2():
    global W,H
    A = read_input()
    H = len(A)
    W = len(A[0])
    X = []
    n,N = len(A[0]), len(A)
    for i in range(N):
        X.append(update(*(-1,i,Dir.RIGHT), A))
        X.append(update(*(n,i,Dir.LEFT), A))
    for i in range(n):
        X.append(update(*(i,-1,Dir.DOWN), A))
        X.append(update(*(i,N,Dir.UP), A))
    
    k = max([run(x,A) for x in X])
    print("Part 2:",k)

part1()
part2()
