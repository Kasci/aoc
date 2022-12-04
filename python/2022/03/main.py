#!/usr/bin/env python3

import sys
sys.path.append("../../")
sys.path.append("../")
import util as u

###############
debug = False
###############

file = "sample.txt" if debug else "input.txt"

def val(a):
    if ord(a) >= ord('a') and ord(a) <= ord('z'):
        return ord(a) - ord('a') + 1
    if ord(a) >= ord('A') and ord(a) <= ord('Z'):
        return ord(a) - ord('A') + 27
    raise Exception('Unknown letter')

def comp(a,b):
    for aa in a:
        if aa in b:
            return val(aa)

def find(a,b,c):
    x = []
    for aa in a:
        if aa in b:
            x.append(aa)
    for xx in x:
        if xx in c:
            return val(xx)

def read_input():
    return u.read_lines(file)

def part1():
    A = read_input()
    B = [comp(a[:len(a)//2], a[len(a)//2:]) for a in A]
    k = sum(B)
    print("Part 1:",k)

def part2():
    A = read_input()
    B = [find(A[3*i], A[3*i+1], A[3*i+2]) for i in range(len(A)//3)]
    k = sum(B)
    print("Part 2:",k)

part1()
part2()
