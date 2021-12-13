#!/usr/bin/env python3

import sys
sys.path.append("../../")
import util as u

###############
debug = False
###############

file = "sample.txt" if debug else "input.txt"

A = []

def read_input():
    return u.read_int_lines(file)

def part1():
    A = read_input()
    k = sum([1 if i+1 < len(A) and A[i] < A[i+1] else 0 for i in range(len(A))])
    print("Part 1:",k)

def part2():
    A = read_input()
    B = [A[i]+A[i+1]+A[i+2] for i in range(len(A)) if i+2 < len(A)]
    k = sum([1 if i+1 < len(B) and B[i] < B[i+1] else 0 for i in range(len(B))])
    print("Part 2:",k)

part1()
part2()
