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
    return u.read_lines(file)[0]

def part1():
    A = read_input()
    k = 0
    for i in range(len(A)-3):
        if A[i] not in A[i+1:i+4] and A[i+1] not in A[i] + A[i+2:i+4] and A[i+2] not in A[i:i+2]+A[i+3] and A[i+3] not in A[i:i+3]:
            k = i+4
            break
    print("Part 1:",k)

def part2():
    A = read_input()
    k = 0
    for i in range(len(A)-13):
        # print(A[i:i+14], set(A[i:i+14]))
        if len(set(A[i:i+14])) == 14:
            k = i+14
            break
    print("Part 2:",k)

part1()
part2()
