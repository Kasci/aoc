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
    return u.read_lines(file)[0].split(",")

def hash(n):
    val = 0
    for a in n:
        val += ord(a)
        val *= 17
        val %= 256
    return val

def part1():
    A = read_input()
    k = 0
    for a in A:
        n = hash(a)
        k += n
    print("Part 1:",k)

def part2():
    A = read_input()
    k = 0
    D = dict()
    for a in A:
        if "=" in a:
            n = a.split("=")
            h = hash(n[0])
            if h in D:
                if any([d[0]==n[0] for d in D[h]]):
                    D[h] = [d if d[0] != n[0] else (n[0], int(n[1])) for d in D[h]]
                else:
                    D[h].append((n[0], int(n[1])))
            else:
                D[h] = [(n[0], int(n[1]))]
        else:
            n = a[:-1]
            h = hash(n)
            if h in D:
                D[h] = [d for d in D[h] if d[0] != n]
            else:
                pass
    for i in range(256):
        if i in D:
            q = 1
            for a in D[i]:
                k += (i+1) * q * a[1]
                q += 1
    print("Part 2:",k)

part1()
part2()
