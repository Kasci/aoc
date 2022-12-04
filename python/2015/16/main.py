#!/usr/bin/env python3

import sys
sys.path.append("../../")
sys.path.append("../")
import util as u

###############
debug = False
###############

file = "sample.txt" if debug else "input.txt"

tape = dict({
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
})

def read_input():
    return [(a,int(b),c,int(d),e,int(f)) for a,b,c,d,e,f in u.read_match(file, ".* (.*): (.*), (.*): (.*), (.*): (.*)")]

def part1():
    A = read_input()
    k = 0
    for i,a in enumerate(A):
        if tape[a[0]] == a[1] and tape[a[2]] == a[3] and tape[a[4]] == a[5]:
            k = i+1
            break
    print("Part 1:",k)

def t(a,v):
    k = tape[a]
    if a in ["cats", "trees"]:
        return k < v
    elif a in ["pomeranians", "goldfish"]:
        return k > v
    else:
        return k == v

def part2():
    A = read_input()
    k = -1
    for i,a in enumerate(A):
        if t(a[0], a[1]) and t(a[2], a[3]) and t(a[4], a[5]):
            k = i+1
            break
    print("Part 2:",k)

part1()
part2()
