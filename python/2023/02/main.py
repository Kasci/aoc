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
    A = u.read_match(file, "Game (\d+): (.*)")
    return [(X[0], [x.split(", ") for x in X[1].split("; ")]) for X in A]

def part1():
    A = read_input()
    k = 0
    for game in A:
        R,G,B = 0,0,0
        for turn in game[1]:
            for val in turn:
                n = val.split(" ")
                i = int(n[0])
                if n[1] == "red" and i > R:
                    R = i
                elif n[1] == "blue" and i > B:
                    B = i
                elif n[1] == "green" and i > G:
                    G = i
        if R <= 12 and G <= 13 and B <= 14:
            k += int(game[0])
    print("Part 1:",k)

def part2():
    A = read_input()
    k = 0
    for game in A:
        R,G,B = 0,0,0
        for turn in game[1]:
            for val in turn:
                n = val.split(" ")
                i = int(n[0])
                if n[1] == "red" and i > R:
                    R = i
                elif n[1] == "blue" and i > B:
                    B = i
                elif n[1] == "green" and i > G:
                    G = i
        k += R*B*G
    print("Part 2:",k)

part1()
part2()
