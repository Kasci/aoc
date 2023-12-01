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

def part1():
    A = read_input()
    k = 0
    for a in A:
        n = [x for x in a if ord(x) >= ord('0') and ord(x) <= ord('9')]
        k += int(n[0]+n[-1])
    print("Part 1:",k)

def part2():
    A = read_input()
    B = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    k = 0
    for a in A:
        n = 0
        for i in range(len(a)):
            x = a[i]
            if ord(x) >= ord('0') and ord(x) <= ord('9'):
                n += ord(x)-ord('0')
                break
            else:
                y = [a[i:].startswith(b) for b in B]
                if any(y):
                    n += y.index(True)+1
                    break
        n *= 10
        for i in range(len(a)):
            x = a[len(a)-1-i]
            if ord(x) >= ord('0') and ord(x) <= ord('9'):
                n += ord(x)-ord('0')
                break
            else:
                y = [a[:len(a)-i].endswith(b) for b in B]
                if any(y):
                    n += y.index(True)+1
                    break
        k += n
    print("Part 2:",k)

part1()
part2()
