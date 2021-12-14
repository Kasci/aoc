#!/usr/bin/env python3

import sys
sys.path.append("../../")
import util as u

###############
debug = False
###############

file = "sample.txt" if debug else "input.txt"

def read_input():
    A = u.read_lines(file)
    N = [int(x) for x in A[0].split(",")]
    M = [A[6*i+2:6*(i+1)+1] for i in range(len(A)//6)]
    B = [[[(int(x),False) for x in a.split(" ") if x != ""] for a in m] for m in M]
    return (N,B)

def board_win(b):
    for i in range(5):
        r,c = True, True
        for j in range(5):
            r &= b[j][i][1]
            c &= b[i][j][1]
        if r or c:
            return True
    return False

def call_num(a,b):
    for i in range(5):
        for j in range(5):
            if b[i][j][0] == a:
                b[i][j] = (a, True)
    return b

def get_first(A,B):
    for a in A:
        for b in B:
            b = call_num(a,b)
        for b in B:
            if board_win(b):
                return sum([n[0] for bb in b for n in bb if not n[1]])*a

def get_all(A,B):
    i = -1
    for a in A:
        for b in B:
            b = call_num(a,b)
        l = sum([1 if board_win(b) else 0 for b in B]) 
        if l == len(B)-1:
            i = [i for i,n in enumerate(B) if not board_win(n)][0]
        if l == len(B):
            return sum([n[0] for bb in B[i] for n in bb if not n[1]])*a

def part1():
    A,B = read_input()
    k = get_first(A,B)
    print("Part 1:",k)

def part2():
    A,B = read_input()
    k = get_all(A,B)
    print("Part 2:",k)

part1()
part2()
