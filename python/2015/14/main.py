#!/usr/bin/env python3

import sys
sys.path.append("../../")
sys.path.append("../")
import util as u

###############
debug = False
###############

file = "sample.txt" if debug else "input.txt"

def step(a, s):
    ret = 0
    (speed, time, rest) = a
    while s > time+rest:
        ret += speed*time
        s -= time+rest
    if s >= time:
        ret += speed*time
    else:
        ret += speed*s
    return ret

def iter(A, n):
    l = [0] * len(A)
    for s in range(n):
        for i,a in enumerate(A):
            l[i] = step(a, s+1)
    return max(l)

def point(A, n):
    l = [0] * len(A)
    p = [0] * len(A)
    for s in range(n):
        for i,a in enumerate(A):
            l[i] = step(a, s+1)
        m = 0
        for i in range(len(A)):
            if m < l[i]:
                m = l[i]
        for i in range(len(A)):
            if l[i] == m:
                p[i] += 1
    return max(p)

def read_input():
    X = u.read_match(file,".* ([0-9]+) .* ([0-9]+) .* ([0-9]+) .*")
    return [(int(x[0]), int(x[1]), int(x[2])) for x in X]

def part1():
    A = read_input()
    k = iter(A, 2503)
    print("Part 1:",k)

def part2():
    A = read_input()
    k = point(A, 2503)
    print("Part 2:",k)

part1()
part2()
