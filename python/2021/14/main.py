#!/usr/bin/env python3

import sys
sys.path.append("../../")
import util as u
from collections import Counter 

###############
debug = False
###############

file = "sample.txt" if debug else "input.txt"

def read_input():
    A = u.read_lines(file)
    d = A[0]
    A = dict([a.split(" -> ") for a in A[2:]])
    return d,A

def iter(d,A):
    dd = d[0]
    for j in range(len(d)-1):
        a = A[d[j:j+2]]
        dd += a + d[j+1]
    return dd

def part1():
    d, A = read_input()
    for i in range(10):
        d = iter(d,A)
    c = Counter(list(d))
    v = sorted(c.values())
    print("Part 1",v[-1]-v[0])

def part2():
    d, A = read_input()
    c = Counter(list(d))
    D = Counter([d[i:i+2] for i in range(len(d)-1)])
    for r in range(40):
        DD = Counter()
        for n in D:
            a = A[n]
            k = D[n]
            if a in c:
                c[a] += k
            else:
                c[a] = k
            if n[0]+a in DD:
                DD[n[0]+a] += k
            else:
                DD[n[0]+a] = k
            if a+n[1] in DD:
                DD[a+n[1]] += k
            else:
                DD[a+n[1]] = k
        D = DD
    v = sorted(c.values())
    print("Part 2",v[-1]-v[0])

part1()
part2()
