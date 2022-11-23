#!/usr/bin/env python3

import sys
sys.path.append("../../")
sys.path.append("../")
import util as u
import util2017 as w

###############
debug = False
###############

file = "sample.txt" if debug else "input.txt"

def read_input():
    return u.read_match(file, "(.+) -> (.+)")

def part1():
    A = read_input()
    k = 0
    d = w.build(A)
    v = dict()
    print("Part 1:",w.execute(d, v,'a'))

def part2():
    A = read_input()
    k = 0
    d = w.build(A)
    d['b'] = ('value', '46065')
    v = dict()
    print("Part 2:",w.execute(d, v,'a'))

part1()
part2()
