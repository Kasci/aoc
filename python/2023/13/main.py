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
    T = u.read_lines(file)
    R = []
    r = []
    for t in T:
        if t == "":
            R.append(r)
            r = []
            continue
        r.append(t)
    R.append(r)
    return R

def merge(a,l,r):
    while l<r and a[l] == a[r]:
        l += 1
        r -= 1
    if l-1 == r:
        return l
    return 0
    
def left(a,l,r):
    while l<r and a[l] != a[r]:
        l += 1
    if l != r:
        return merge(a,l,r)
    return 0

def right(a,l,r):
    while l<r and a[l] != a[r]:
        r -= 1
    if l != r:
        return merge(a,l,r)
    return 0

def find(a):
    L,R = 0,len(a)-1
    while L < R:
        l,r = L,len(a)-1
        n = left(a,l,r)
        if n == 0:
            L += 1
        else:
            return n
    L,R = 0,len(a)-1
    while L < R:
        l,r = 0,R
        n = right(a,l,r)
        if n == 0:
            R -= 1
        else:
            return n
    return 0

def findAll(a):
    Q = []
    L,R = 0,len(a)-1
    while L < R:
        l,r = L,len(a)-1
        n = left(a,l,r)
        if n != 0:
            Q.append(n)
        L += 1

    L,R = 0,len(a)-1
    while L < R:
        l,r = 0,R
        n = right(a,l,r)
        if n != 0:
            Q.append(n)
        R -= 1
    return Q

def getAll(a):
    r = []
    n = findAll(a)
    r.extend([100*q for q in n])
    a = ["".join([x[i] for x in a]) for i in range(len(a[0]))]
    r.extend(findAll(a))
    return r
    
def get(a):
    n = find(a)
    if n == 0:
        a = ["".join([x[i] for x in a]) for i in range(len(a[0]))]
        return find(a)
    else:
        return 100*n
    
def getN(a, n):
    for i in range(len(a)):
        for j in range((len(a[0]))):
            b = [[x for x in aa] for aa in a]
            if b[i][j] == ".":
                b[i][j] = "#"
            else: 
                b[i][j] = "."
            m = list(set(getAll(b)))
            if n in m:
                m.remove(n)
            if len(m) == 1:
                return m[0]
    return 0

    
def part1():
    A = read_input()
    k = 0
    for a in A:
        k += get(a)    
    print("Part 1:",k)

def part2():
    A = read_input()
    k = 0
    for a in A:
        n = get(a)
        k += getN(a, n)
    print("Part 2:",k)

part1()
part2()
