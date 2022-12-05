#!/usr/bin/env python3

import io
import re
import sys
sys.path.append("../../")
sys.path.append("../")
import util as u

###############
debug = False
###############

file = "sample.txt" if debug else "input.txt"

def read_input():
    A, B = [], []
    b = False
    with io.open(file,"r") as f:
        while True:
            a = f.readline()
            if a == "" or a == None:
                break
            a = a.replace("\n","")
            if len(a) == 0:
                b = True
                continue
            if b:
                B.append(a)
            else:
                A.append(a)
    return A, B

def create_stacks(A):
    n = sum([1 for a in A[-1].split(" ") if len(a) > 0])
    K = []
    for i in range(n):
        k = []
        for j in range(len(A)-2, -1, -1):
            p = A[j][1+4*i]
            if p != ' ':
                k.append(p)
        K.append(k)
    return K

def create_instructions(B):
    return [[int(a) for a in re.match("move (.+) from (.+) to (.+)",b).groups()] for b in B]

def step(K, inst):
    for i in range(inst[0]):
        K[inst[2]-1].append(K[inst[1]-1].pop())
    return K

def step_plus(K, inst):
    t = []
    for i in range(inst[0]):
        t.append(K[inst[1]-1].pop())
    for _ in range(len(t)):
        K[inst[2]-1].append(t.pop())
    return K

def execute_instructions(K, I):
    for i in I:
        K = step(K, i)
    r = ""
    for k in K:
        r += k.pop()
    return r

def execute_instructions_plus(K, I):
    for i in I:
        K = step_plus(K, i)
    r = ""
    for k in K:
        r += k.pop()
    return r

def part1():
    A, B = read_input()
    K = create_stacks(A)
    I = create_instructions(B)
    k = execute_instructions(K, I)
    print("Part 1:",k)

def part2():
    A, B = read_input()
    K = create_stacks(A)
    I = create_instructions(B)
    k = execute_instructions_plus(K, I)
    print("Part 2:",k)

part1()
part2()
