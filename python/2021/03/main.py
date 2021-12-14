#!/usr/bin/env python3

import sys
sys.path.append("../../")
import util as u

###############
debug = False
###############

file = "sample.txt" if debug else "input.txt"

def read_input():
    return u.read_lines(file)

def part1():
    A = read_input()

    size = len(A[0])
    c = [0 for i in range(size)]
    for a in A:
        for i in range(size):
            c[i] += int(a[i])
    g = [1 if s > len(A)//2 else 0 for s in c]
    e = [0 if s > len(A)//2 else 1 for s in c]
    
    gamma = 0
    for x in g:
        gamma = gamma * 2 + x

    epsilon = 0
    for x in e:
        epsilon = epsilon * 2 + x

    k = gamma*epsilon
    print("Part 1:",k)

def part2():
    A = read_input()
    
    size = len(A[0])
    c = [0 for i in range(size)]

    for i in range(size):
        for a in A:
            c[i] += int(a[i])
        A = [a for a in A if a[i] == ("1" if c[i] >= len(A)/2 else "0")]
        if len(A) == 1:
            break
    oxygen = A[0]

    A = read_input()
    c = [0 for i in range(size)]
    for i in range(size):
        for a in A:
            c[i] += int(a[i])
        A = [a for a in A if a[i] == ("0" if c[i] >= len(A)/2 else "1")]
        if len(A) == 1:
            break
    co2 = A[0]

    k = int(oxygen,2)*int(co2,2)
    print("Part 2:",k)

part1()
part2()
