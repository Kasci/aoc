#!/usr/bin/env python3

import sys
sys.path.append("../../")
import util as u

###############
debug = True
###############

file = "sample.txt" if debug else "input.txt"

def read_input():
    return u.read_lines(file)

def part1():
    A = read_input()
    k = 0
    print("Part 1:",k)
    raise Exception("Not implemented")  

def part2():
    A = read_input()
    k = 0
    print("Part 2:",k)
    raise Exception("Not implemented")  

part1()
part2()
