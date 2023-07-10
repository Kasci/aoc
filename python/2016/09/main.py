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
    return u.read_lines(file)

def evaluate(a, b):
    i = 0
    ret = 0 
    while i < len(a):
        if a[i] == '(':
            j = i
            while a[j] != ')':
                j+=1
            j+=1
            s = a[i:j]
            x = 0
            while s[x] != 'x':
                x+=1
            l = int(s[1:x])
            t = int(s[x+1:-1])
            if b:
                m = evaluate(a[j:j+l], b)
                ret += t*m
            else:
                ret += t*len(a[j:j+l])
            i = j + l
        else: 
            ret += 1
            i += 1
    return ret

def part1():
    A = read_input()
    k = 0
    for a in A:
        n = evaluate(a, False)
        k += n
    print("Part 1:",k)

def part2():
    A = read_input()
    k = 0
    for a in A:
        n = evaluate(a, True)
        k += n
    print("Part 2:",k)

part1()
part2()
