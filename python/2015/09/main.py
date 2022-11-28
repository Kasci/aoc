#!/usr/bin/env python3

import sys
sys.path.append("../../")
sys.path.append("../")
import util as u

###############
debug = False
###############

file = "sample.txt" if debug else "input.txt"

def min(arr):
    return sorted(arr)[0]

def max(arr):
    return sorted(arr)[-1]

def path(used, all, ssum, method):
    last = used[-1]
    app = [x for x in all if x[0] not in used[:-1] and x[1] not in used[:-1]]
    valid = [(x[0], x[1], x[2]) if x[0] == last else (x[1], x[0], x[2]) if x[1] == last else None for x in app]
    valid = [x for x in valid if x is not None]
    if (len(valid) == 0):
        return ssum
    else:
        return method([path(used + [n[1]], app, ssum + int(n[2]), method) for n in valid])

def read_input():
    return u.read_match(file, "(.*) to (.*) = (.*)")

def part1():
    A = read_input()
    a = set([a[0] for a in A] + [a[1] for a in A])
    k = min([path([x], A, 0, min) for x in a])
    print("Part 1:",k)

def part2():
    A = read_input()
    a = set([a[0] for a in A] + [a[1] for a in A])
    k = max([path([x], A, 0, max) for x in a])
    print("Part 2:",k)
    
part1()
part2()
