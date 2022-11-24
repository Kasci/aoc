#!/usr/bin/env python3

import sys
sys.path.append("../../")
sys.path.append("../")
import util as u
import re

###############
debug = False
###############

file = "sample.txt" if debug else "input.txt"

def analyze(a):
    l = len(a)
    a = a.replace("\\\\","*")
    a = a.replace("\\\"","+")
    a = re.sub("\\\\x[0-9a-f][0-9a-f]","-", a)
    return (l,len(a)-2)

def encode(a):
    l = len(a)
    a = a.replace("\\", "\\\\")
    a = a.replace("\"", "\\\"")
    return (len(a)+2, l)

def read_input():
    return u.read_lines(file)

def part1():
    A = read_input()
    l = [analyze(a) for a in A]
    print("Part 1:",sum([i[0] for i in l]) - sum([i[1] for i in l]))

def part2():
    A = read_input()
    l = [encode(a) for a in A]
    print("Part 2:",sum([i[0] for i in l]) - sum([i[1] for i in l]))

part1()
part2()
