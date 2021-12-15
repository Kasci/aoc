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
    return u.read_match(file, "(\w+)-(\w+)")

def path_rec(node, D, path):
    lst = []
    if node == "end":
        return [path]
    for n in D[node]:
        if n[0] <= "z" and n[0] >= "a" and n in path:
            continue
        p = path_rec(n, D, path + [n])
        lst.extend(p)
    return lst

def path_rec2(node, D, path):
    lst = []
    if node == "end":
        return [path]
    for n in D[node]:
        c = Counter([x for x in path if x[0] >= "a" and x[0] <= "z"])
        if n[0] <= "z" and n[0] >= "a" and ((n in path and 2 in c.values()) or n == "start"):
           continue
        p = path_rec2(n, D, path + [n])
        lst.extend(p)
    return lst

def part1():
    A = read_input()
    D = {}
    for d in list(set([x for a in A for x in [a[0],a[1]]])):
        D[d] = [a[1] for a in A if a[0] == d] + [a[0] for a in A if a[1] == d]
    N = path_rec("start",D,["start"])
    k = len(N) 
    print("Part 1:",k)

def part2():
    A = read_input()
    D = {}
    for d in list(set([x for a in A for x in [a[0],a[1]]])):
        D[d] = [a[1] for a in A if a[0] == d] + [a[0] for a in A if a[1] == d]
    N = path_rec2("start",D,["start"])
    k = len(N) 
    print("Part 2:",k)

part1()
part2()
