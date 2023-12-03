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

def check(A, i, j):
    for x in range(3):
        for y in range(3):
            if i+x-1 < 0 or i+x-1 >= len(A) or j+y-1 < 0 or j+y-1 >= len(A[0]):
                continue
            if A[i+x-1][j+y-1] not in ['.']+[chr(ord('0')+x) for x in range(10)]:
                return True
    return False

def check2(A, i, j):
    for x in range(3):
        for y in range(3):
            if i+x-1 < 0 or i+x-1 >= len(A) or j+y-1 < 0 or j+y-1 >= len(A[0]):
                continue
            if A[i+x-1][j+y-1] == "*":
                return (i+x-1,j+y-1)
    return (0,0)

def part1():
    A = read_input()
    k = 0
    i = 0
    while i < len(A):
        j = 0
        while j < len(A[i]):
            marked = False
            kk = 0
            while j < len(A[0]) and A[i][j] in [chr(ord('0')+x) for x in range(10)]:
                kk = kk*10 + int(A[i][j])
                marked |= check(A,i,j)
                A[i].replace(A[i][j],'.',1)
                j += 1
            # print(i,j, marked, kk)
            k += kk if marked else 0
            j += 1
        i += 1
    print("Part 1:",k)

def part2():
    A = read_input()
    M = []
    i = 0
    while i < len(A):
        j = 0
        while j < len(A[i]):
            marked = False
            kk = 0
            t = (0,0)
            mt = (0,0)
            while j < len(A[0]) and A[i][j] in [chr(ord('0')+x) for x in range(10)]:
                kk = kk*10 + int(A[i][j])
                t = check2(A,i,j)
                if t != (0,0):
                    marked = True
                    mt = t
                A[i].replace(A[i][j],'.',1)
                j += 1
            # print(i,j, marked, kk)
            if marked:
                for m in M:
                    if m[0] == mt[0]*200+mt[1]:
                        m[1] *= kk
                        m[2] += 1
                        # print(">", mt, kk)
                        break
                else:
                    # print(".", mt, kk)
                    M.append([mt[0]*200+mt[1], kk, 1])
            j += 1
        i += 1
    # print(M)
    k = sum([m[1] for m in M if m[2]==2])
    print("Part 2:",k)

part1()
part2()
