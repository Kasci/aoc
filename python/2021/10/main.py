#!/usr/bin/env python3

import sys
sys.path.append("../../")
import util as u

###############
debug = False
###############

file = "sample.txt" if debug else "input.txt"

d = {
    "(": 3,
    "[": 57,
    "{": 1197,
    "<": 25137
}
dd = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4
}
    
b = { "}":"{", "]":"[", ")":"(", ">":"<" }

def read_input():
    return u.read_lines(file)

def part1():
    A = read_input()
    k = 0
    for a in A:
        l = []
        for p in a:
            if p in ["(","[","{","<"]:
                l.append(p)
            else:
                n = l.pop()
                if (p == ")" and n == "(") or (p == "]" and n == "[") or (p == "}" and n == "{") or (p == ">" and n == "<"): 
                    continue
                k += d[b[p]]
                break
    print("Part 1:",k)

def part2():
    A = read_input()
    w = []
    for a in A:
        l = []
        kk = 0
        good = True
        for p in a:
            if p in ["(","[","{","<"]:
                l.append(p)
            else:
                n = l.pop()
                if (p == ")" and n == "(") or (p == "]" and n == "[") or (p == "}" and n == "{") or (p == ">" and n == "<"): 
                    continue
                good = False
                break
        if good:    
            for ll in l[-1::-1]:
                kk *= 5
                kk += dd[ll]
            w.append(kk)
    k = sorted(w)[len(w)//2]
    print("Part 2:",k)

part1()
part2()
