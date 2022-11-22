#!/usr/bin/env python3

import sys
sys.path.append("../../")
import util as u

import hashlib

###############
debug = False
###############

file = "sample.txt" if debug else "input.txt"

def read_input():
    return "abcdef" if debug else "bgvyzdsv"

def part1():
    A = read_input()
    k = 0
    while True:
        s = A + str(k)
        w = hashlib.md5(s.encode()).hexdigest()[0:5]
        if w == "00000":
            break
        k+=1
    print("Part 1:",k)

def part2():
    A = read_input()
    k = 0
    while True:
        s = A + str(k)
        w = hashlib.md5(s.encode()).hexdigest()[0:6]
        if w == "000000":
            break
        k+=1
    print("Part 2:",k)

part1()
part2()