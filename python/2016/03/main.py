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
    return [(int(a[0]),int(a[1]),int(a[2])) for a in u.read_match(file,"(\d+)\s+(\d+)\s+(\d+)")]

def part1():
    A = read_input()
    k = sum([1 if a[0]+a[1] > a[2] and a[0]+a[2] > a[1] and a[1]+a[2] > a[0] else 0 for a in A])
    print("Part 1:",k)

def part2():
    A = read_input()
    B = [(A[3*i][j], A[3*i+1][j], A[3*i+2][j]) for j in range(3) for i in range(len(A)//3)]
    k = sum([1 if a[0]+a[1] > a[2] and a[0]+a[2] > a[1] and a[1]+a[2] > a[0] else 0 for a in B])
    print("Part 2:",k)

part1()
part2()
