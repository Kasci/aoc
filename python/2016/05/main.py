#!/usr/bin/env python3

import sys
sys.path.append("../../")
sys.path.append("../")
import util as u

import hashlib

###############
debug = False
###############

file = "sample.txt" if debug else "input.txt"

def read_input():
    return u.read_lines(file)[0]

def part1():
    A = read_input()
    k = ""
    n = 0
    while True:
        h = hashlib.md5((A+str(n)).encode()).hexdigest()
        if h[0:5] == "00000":
            k += h[5]
        n += 1
        if len(k) == 8:
            break
    print("Part 1:",k)


def part2():
    A = read_input()
    k = [" " for _ in range(8)] 
    n = 0
    while True:
        h = hashlib.md5((A+str(n)).encode()).hexdigest()
        if h[0:5] == "00000" and '0' <= h[5] <= '7' and k[ord(h[5])-ord('0')] == " ":
            k[ord(h[5])-ord('0')] = h[6]
        n += 1
        if " " not in k:
            break
    print("Part 2:","".join(k))

part1()
part2()
