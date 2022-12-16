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

def traverse(A,B,P,E):
    i = 0
    while len(P) > 0:
        t = P.pop(0)
        current = B[t[0]][t[1]]
        if t[0]-1 >= 0 and ord(A[t[0]-1][t[1]]) - ord(A[t[0]][t[1]]) <= 1 and current < B[t[0]-1][t[1]] and (t[0]-1,t[1]) not in P:
            P.append((t[0]-1,t[1]))
        if t[1]-1 >= 0 and ord(A[t[0]][t[1]-1]) - ord(A[t[0]][t[1]]) <= 1 and current < B[t[0]][t[1]-1] and (t[0],t[1]-1) not in P:
            P.append((t[0],t[1]-1))
        if t[0]+1 < len(A) and ord(A[t[0]+1][t[1]]) - ord(A[t[0]][t[1]]) <= 1 and current < B[t[0]+1][t[1]] and (t[0]+1,t[1]) not in P:
            P.append((t[0]+1,t[1]))
        if t[1]+1 < len(A[0]) and ord(A[t[0]][t[1]+1]) - ord(A[t[0]][t[1]]) <= 1 and current < B[t[0]][t[1]+1] and (t[0],t[1]+1) not in P:
            P.append((t[0],t[1]+1))
        for p in P:
            if current+1 < B[p[0]][p[1]]:
                B[p[0]][p[1]] = current+1
        # if i%100 == 0:
        #     print(len(P))
        # print(P)
        # if i == 10:
        #     break
        i += 1
    # print(B)
    return B[E[0]][E[1]]

def part1():
    A = read_input()
    B = [[999 for _ in a] for a in A]
    S = [[(i,j) for j,b in enumerate(a) if b == "S"] for i,a in enumerate(A) if "S" in a][0][0]
    A[S[0]] = A[S[0]].replace('S','a')
    E = [[(i,j) for j,b in enumerate(a) if b == "E"] for i,a in enumerate(A) if "E" in a][0][0]
    A[E[0]] = A[E[0]].replace('E','z')
    P = [S]
    B[S[0]][S[1]] = 0
    k = traverse(A,B,P,E)
    print("Part 1:",k)

def part2():
    A = read_input()
    E = [[(i,j) for j,b in enumerate(a) if b == "E"] for i,a in enumerate(A) if "E" in a][0][0]
    A[E[0]] = A[E[0]].replace('E','z')
    S = [[(i,j) for j,b in enumerate(a) if b == "S"] for i,a in enumerate(A) if "S" in a][0][0]
    A[S[0]] = A[S[0]].replace('S','a')
    k = 999
    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j] == 'a':
                S = (i,j)
                B = [[999 for _ in a] for a in A]
                B[S[0]][S[1]] = 0
                P = [S]
                m = traverse(A,B,P,E)
                if m < k:
                    k = m
    print("Part 2:",k)

part1()
part2()
