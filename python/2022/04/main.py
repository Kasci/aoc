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
    return u.read_match(file,"(.*)-(.*),(.*)-(.*)")

def part1():
    A = read_input()
    k = sum([1 if (int(a)<=int(c) and int(b)>=int(d))or (int(a)>=int(c) and int(b)<=int(d)) else 0 for a,b,c,d in A])
    print("Part 1:",k)

def part2():
    A = read_input()
    k = sum([1 if not ((int(b)<int(c) )or (int(a)>int(d))) else 0 for a,b,c,d in A])
    print("Part 2:",k)

part1()
part2()
