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
    return [[int(y) for y in x.split(" ")] for x in u.read_lines(file)]

def part1():
    A = read_input()
    k = 0
    for a in A:
        N = [a]
        i = 0
        while True:
            n = [N[i][x+1]-N[i][x] for x in range(len(N[i])-1)]
            if all([x == 0 for x in n]):
                break
            N.append(n)
            i+=1
        t = [n[-1] for n in N]
        k += sum(t)
    print("Part 1:",k)

def part2():
    A = read_input()
    k = 0
    for a in A:
        N = [a]
        i = 0
        while True:
            n = [N[i][x+1]-N[i][x] for x in range(len(N[i])-1)]
            if all([x == 0 for x in n]):
                break
            N.append(n)
            i+=1
        t = [n[0] if i%2==0 else -n[0] for i,n in enumerate(N)]
        k += sum(t)
    print("Part 2:",k)

part1()
part2()
