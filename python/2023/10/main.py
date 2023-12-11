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
    return [[x for x in A] for A in u.read_lines(file)]

def printMap(A):
    for a in A:
        print("".join(a))

def findS(A):
    for i,a in enumerate(A):
        for j,b in enumerate(a):
            if b == "S":
                return (j,i)

def firstStep(A,x,y):
    if A[y][x+1] in ["-","7","J"]:
        return 1
    if A[y+1][x] in ["|","L","J"]:
        return 2
    if A[y][x-1] in ["-","F","L"]:
        return 3
    if A[y-1][x] in ["|","F","7"]:
        return 0
    
def firstStep2(A,x,y):
    ss = []
    if A[y][x+1] in ["-","7","J"]:
        ss.append(1)
    if A[y+1][x] in ["|","L","J"]:
        ss.append(2)
    if A[y][x-1] in ["-","F","L"]:
        ss.append(3)
    if A[y-1][x] in ["|","F","7"]:
        ss.append(0)
    return ss

def nextStep(A,s,x,y):
    if s == 0:
        if A[y-1][x] == "|":
            return (0,y-1,x)
        if A[y-1][x] == "F":
            return (1,y-1,x)
        if A[y-1][x] == "7":
            return (3,y-1,x)
    if s == 1:
        if A[y][x+1] == "-":
            return (1,y,x+1)
        if A[y][x+1] == "7":
            return (2,y,x+1)
        if A[y][x+1] == "J":
            return (0,y,x+1)
    if s == 2:
        if A[y+1][x] == "|":
            return (2,y+1,x)
        if A[y+1][x] == "L":
            return (1,y+1,x)
        if A[y+1][x] == "J":
            return (3,y+1,x)
    if s == 3:
        if A[y][x-1] == "-":
            return (3,y,x-1)
        if A[y][x-1] == "F":
            return (2,y,x-1)
        if A[y][x-1] == "L":
            return (0,y,x-1)

def part1():
    A = read_input()
    k = 0
    x,y = findS(A)
    s = firstStep(A,x,y)
    while True:
        N = nextStep(A,s,x,y)
        if N == None:
            break
        s,y,x = N
        # print(s,x,y,A[y][x])
        k += 1
    print("Part 1:",(k+1)//2)

def color(ss,B,x,y):
    B[3*y+1][3*x+1] = "O"
    if 0 in ss:
        B[3*y][3*x+1] = "O"
    if 1 in ss:
        B[3*y+1][3*x+2] = "O"
    if 2 in ss:
        B[3*y+2][3*x+1] = "O"
    if 3 in ss:
        B[3*y+1][3*x] = "O"
    if 0 in ss and 1 in ss:
        return (3*x+2,3*y)
    if 1 in ss and 2 in ss:
        return (3*x+2,3*y+2)
    if 2 in ss and 3 in ss:
        return (3*x,3*y+2)
    if 3 in ss and 0 in ss:
        return (3*x,3*y)

def part2():
    A = read_input()
    B = [["." for _ in range(len(A[0])*3)] for _ in range(len(A)*3)]
    k = 0
    q = 0
    x,y = findS(A)
    ss = firstStep2(A,x,y)
    a,b = color(ss,B,x,y)
    L = [(a,b)]
    s = ss[0]
    while True:
        oldS = (s+2)%4
        N = nextStep(A,s,x,y)
        if N == None:
            break
        s,y,x = N
        color([oldS,s],B,x,y)
    color([oldS,s],B,x,y)
    while len(L) > 0:
        a,b = L.pop()
        B[b][a] = "+"
        if b-1 >= 0 and B[b-1][a] == ".":
            L.append((a,b-1))
        if a-1 >= 0 and B[b][a-1] == ".":
            L.append((a-1,b))
        if b+1 < len(B) and B[b+1][a] == ".":
            L.append((a,b+1))
        if a+1 < len(B[0]) and B[b][a+1] == ".":
            L.append((a+1,b))
    for i in range(len(A)):
        for j in range(len(A[0])):
            kk = 0
            qq = 0
            for q in range(9):
                # print(B[3*i+q//3][3*j+q%3], end="")
                kk += 1 if B[3*i+q//3][3*j+q%3] == "+" else 0
                qq += 1 if B[3*i+q//3][3*j+q%3] == "." else 0
            # print(" ",end="")
            k += 1 if kk == 9 else 0
            q += 1 if qq == 9 else 0
        # print()
    print("Part 2:",k," or ",q) 

part1()
part2()
print("""
      This uncertainty comes from not being sure, 
      if any L shaped pipe marked as S contains the
      inside or the outside. We could assume, that if
      the TL corner is marked as inside, we should take
      the other answer, but for now it is good.""")
