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

def part1():
    A = read_input()
    N = len(A)
    k = 0
    for i in range(len(A[0])):
        B = [a[i] for a in A]
        for a in range(len(B)-1, -1, -1):
            for b in range(a, len(B)-1):
                if B[b] == "." and B[b+1] == "O":
                    B[b] = "O"
                    B[b+1] = "."
        n = N
        for b in B:
            if b == "O":
                k += n
            n -= 1
    print("Part 1:",k)

def bubble(B):
    for a in range(len(B)-1, -1, -1):
        for b in range(a, len(B)-1):
            if B[b] == "." and B[b+1] == "O":
                B[b] = "O"
                B[b+1] = "."
    return B

def printM(A):
    for a in A:
        print("".join(a))
    print()

def N(A):
    C = []
    for i in range(len(A[0])):
        B = [a[i] for a in A]
        C.append(bubble(B))
    A = []
    for i in range(len(C[0])):
        B = [a[i] for a in C]
        A.append(B)
    return A

def W(A):
    C = []
    for B in A:
        C.append(bubble(B))
    return C

def S(A):
    C = []
    for i in range(len(A[0])):
        B = [a[i] for a in A]
        B.reverse()
        D = bubble(B)
        D.reverse()
        C.append(D)
    A = []
    for i in range(len(C[0])):
        B = [a[i] for a in C]
        A.append(B)
    return A
        
def E(A):
    C = []
    for B in A:
        D = [b for b in B]
        D.reverse()
        B = bubble(D)
        B.reverse()
        C.append("".join(B))
    return C

        
def part2():
    A = read_input()
    R = []
    D = dict()
    L = []
    while True:
        A=N(A)
        A=W(A)
        A=S(A)
        A=E(A)
        M = "".join(A)
        if M in D:
            off = L.index(M)
            c = len(D) - off
            idx = (1000000000 - off) % c - 1 + off 
            R = D[L[idx]]
            break
        else:
            D[M] = A
            L.append(M)
    NN = len(R)
    k = 0
    for i in range(len(R[0])):
        B = [a[i] for a in R]
        n = NN
        for b in B:
            if b == "O":
                k += n
            n -= 1
    print("Part 2:",k)

part1()
part2()
