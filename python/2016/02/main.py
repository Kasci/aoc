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
    k = ""
    Q = [['1','2','3'],['4','5','6'],['7','8','9']]
    x,y = 1,1
    for a in A:
        for i in a:
            if i == "U":
                if y > 0:
                    y -= 1
            elif i == "D":
                if y < 2:
                    y += 1
            elif i == "L":
                if x > 0:
                    x -= 1
            elif i == "R":
                if x < 2:
                    x += 1
        k += Q[y][x]
    print("Part 1:",k)

def part2():
    A = read_input()
    k = ""
    Q = [[None,None,'1',None,None],[None,'2','3','4',None],['5','6','7','8','9'],[None,'A','B','C',None],[None,None,'D',None,None]]
    x,y = 0,2
    for a in A:
        for i in a:
            if i == "U":
                if y > 0 and Q[y-1][x] != None:
                    y -= 1
            elif i == "D":
                if y < 4 and Q[y+1][x] != None:
                    y += 1
            elif i == "L":
                if x > 0 and Q[y][x-1] != None:
                    x -= 1
            elif i == "R":
                if x < 4 and Q[y][x+1] != None:
                    x += 1
        k += Q[y][x]
    print("Part 2:",k)

part1()
part2()
