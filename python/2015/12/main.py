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

def read_input():
    return u.read_lines(file)[0]

def part1():
    A = read_input()
    a = "".join([' ' if x not in ['0','1','2','3','4','5','6','7','8','9','-'] else x for x in A])
    k = sum([int(x) if len(x) > 0 else 0 for x in a.split(" ")])
    print("Part 1:",k)

def part2():
    A = read_input()
    a = "".join([' ' if x not in ['0','1','2','3','4','5','6','7','8','9','-','{','}','[',']','r','e','d'] else x for x in A])
    a = a.replace('[',' [ ')
    a = a.replace(']',' ] ')
    a = a.replace('{',' { ')
    a = a.replace('}',' } ')
    a = a.replace(" ree ", "")
    a = a.replace(" r ", "")
    a = a.replace(" e ", "")
    a = a.replace(" d ", "")
    a = a.split(" ")
    k = 0
    tmp = 0
    tmp_red = False
    partial = []
    is_red = []
    for x in a:
        if len(x) == 0:
            continue
        if x == '{' or x == '[':
            partial.append(tmp)
            is_red.append(tmp_red)
            tmp_red = False
            tmp = 0
        elif x == '}':
            if not tmp_red and len(partial) > 0:
                tmp += partial.pop()
                tmp_red = is_red.pop()
            elif not tmp_red:
                k = tmp
            elif tmp_red and len(partial) > 0:
                tmp = partial.pop()
                tmp_red = is_red.pop()
            else:
                k = 0
        elif x == ']':
            if len(partial) > 0:
                tmp += partial.pop()
                tmp_red = is_red.pop()
            else:
                k = tmp
        elif x == 'red':
            tmp_red = True
        else:
            tmp += int(x)
    k = tmp
    print("Part 2:",k)

part1()
part2()
