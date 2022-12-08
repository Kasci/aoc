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
    return [[int(y) for y in x] for x in u.read_lines(file)]

def bigger_than(A, a):
    ret = True
    for b in A:
        ret &= a > b
    return ret

def count_trees(A):
    B = [[True for _ in range(len(A))] if j == 0 or j == len(A)-1 else [True if i == 0 or i == len(A)-1 else False for i in range(len(A))] for j in range(len(A))]
    for i,a in enumerate(A):
        k = [bigger_than(A[i][0:j+1], A[i][j+1]) for j in range(len(A)-1)]
        for j,b in enumerate(k):
            B[i][j+1] |= b
        l = [bigger_than(A[i][j:], A[i][j-1]) for j in range(len(A)-1,0,-1)]
        for j,b in enumerate(l):
            B[i][len(A) - 2 - j] |= b
    for i,a in enumerate(A):
        AA = [A[x][i] for x in range(len(A))]
        k = [bigger_than(AA[0:j+1], AA[j+1]) for j in range(len(AA)-1)]
        for j,b in enumerate(k):
            B[j+1][i] |= b
        l = [bigger_than(AA[j:], AA[j-1]) for j in range(len(AA)-1,0,-1)]
        for j,b in enumerate(l):
            B[len(A) - 2 - j][i] |= b
    return sum([1 if b else 0 for x in B for b in x])

def count_bigger(x, A):
    r = 0
    for a in A:
        r+=1
        if x <= a:
            break
    return r

def count_view(i,j,A):
    t = A[i][j]
    a = A[i][0:j]
    a.reverse()
    b = A[i][j+1:]
    AA = [A[x][j] for x in range(len(A))]
    c = AA[0:i]
    c.reverse()
    d = AA[i+1:]
    return count_bigger(t,a)*count_bigger(t,b)*count_bigger(t,c)*count_bigger(t,d)

def scenic_score(A):
    x = 0
    for i in range(len(A)):
        for j in range(len(A)):
            t = count_view(i,j,A)
            if t > x:
                x = t
    return x    

def part1():
    A = read_input()
    k = count_trees(A)
    print("Part 1:",k)

def part2():
    A = read_input()
    k = scenic_score(A)
    print("Part 2:",k)

part1()
part2()
