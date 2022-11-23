#!/usr/bin/env python3

import sys
sys.path.append("../../")
import util as u

###############
debug = False
###############

file = "sample.txt" if debug else "input.txt"

def is_nice1(str):
    a = sum([1 if a in "aeiou" else 0 for a in str]) >= 3 
    b = sum([1 if str[i] == str[i+1] else 0 for i in range(len(str)-1)]) > 0
    c = sum([1 if str[i:i+2] in ["ab", "cd", "pq", "xy"] else 0 for i in range(len(str)-1)]) == 0
    return a and b and c

def is_nice2(str):
    a = sum([1 if str[i:i+2] in str[i+2:] else 0 for i in range(len(str)-2)]) > 0
    b = sum([1 if str[i] == str[i+2] else 0 for i in range(len(str)-2)]) > 0
    return a and b

def read_input():
    return u.read_lines(file)

def part1():
    A = read_input()
    k = sum([1 if is_nice1(a) else 0 for a in A])
    print("Part 1:",k)

def part2():
    A = read_input()
    k = sum([1 if is_nice2(a) else 0 for a in A])
    print("Part 2:",k)

part1()
part2()
