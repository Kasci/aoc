#!/usr/bin/env python3

import sys
sys.path.append("../../")
sys.path.append("../")
import util as u

###############
debug = False
###############

file = "sample.txt" if debug else "input.txt"
val1 = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14
}
val2 = {
    "J": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "Q": 12,
    "K": 13,
    "A": 14
}

def read_input():
    return u.read_lines(file)

def eval1(hand):
    n = 0
    for v in hand:
        n += val1[v]
        n *= 20
    return n
def eval2(hand):
    n = 0
    for v in hand:
        n += val2[v]
        n *= 20
    return n

def hType1(hand):
    v = set([h for h in hand])
    if len(v) == 1:
        return 7 # five of kind
    if len(v) == 2:
        if sum([1 for h in hand if h == list(v)[0]]) in [1,4]:
            return 6 # four of kind
        else:
            return 5 # full house
    if len(v) == 3:
        if any([sum([1 for h in hand if h == w])==3 for w in list(v)]):
            return 4 # three of kind
        else:
            return 3 # two pairs
    if len(v) == 4:
        return 2 # pair
    if len(v) == 5:
        return 1 #high card

def hType2(hand):
    v = set([h for h in hand])
    if "J" in v:
        v.remove("J") 
    if len(v) == 1 or len(v) == 0:
        return 7 # five of kind
    if len(v) == 2:
        if any([sum([1 for h in hand if (h == w or h == "J")])==4 for w in list(v)]):
            return 6 # four of kind
        else:
            return 5 # full house
    if len(v) == 3:
        if any([sum([1 for h in hand if (h == w or h == "J")])==3 for w in list(v)]):
            return 4 # three of kind
        else:
            return 3 # two pairs
    if len(v) == 4:
        return 2 # pair
    if len(v) == 5:
        return 1 #high card

def part1():
    A = read_input()
    k = 0
    N = []
    for a in A:
        h, v = a.split(" ")
        N.append((h, hType1(h), eval1(h), v))
    N.sort(key= lambda x: x[2])
    N.sort(key= lambda x: x[1])
    for i,n in enumerate(N):
        k += (i+1)*int(n[3])
    print("Part 1:",k)

def part2():
    A = read_input()
    k = 0
    N = []
    for a in A:
        h, v = a.split(" ")
        N.append((h, hType2(h), eval2(h), v))
    N.sort(key= lambda x: x[2])
    N.sort(key= lambda x: x[1])
    for i,n in enumerate(N):
        k += (i+1)*int(n[3])
    print("Part 2:",k)

part1()
part2()
