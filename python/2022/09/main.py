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
    return [(a[0], int(a[1])) for a in u.read_match(file, "([A-Z]) ([0-9]+)")]

def part1():
    A = read_input()
    H = [0, 0]
    T = [0, 0]
    S = []
    for a in A:
        for i in range(a[1]):
            if a[0] == "U":
                H[1]+=1
            elif a[0] == "D":
                H[1]-=1
            elif a[0] == "R":
                H[0]+=1
            elif a[0] == "L":
                H[0]-=1
            if T[0] == H[0] and abs(T[1]-H[1]) > 1:
                T[1] += 1 if H[1]-T[1] > 0 else -1
            elif T[1] == H[1] and abs(T[0]-H[0]) > 1:
                T[0] += 1 if H[0]-T[0] > 0 else -1
            elif abs(T[0]-H[0]) > 1 or abs(T[1]-H[1]) > 1:
                T[0] += 1 if H[0]-T[0] > 0 else -1
                T[1] += 1 if H[1]-T[1] > 0 else -1
            S.append(str(T[0]) + "|" + str(T[1]))
    k = len(set(S))
    print("Part 1:",k)

def part2():
    A = read_input()
    T = [[0, 0] for _ in range(10)]
    S = []
    for a in A:
        for i in range(a[1]):
            if a[0] == "U":
                T[0][1]+=1
            elif a[0] == "D":
                T[0][1]-=1
            elif a[0] == "R":
                T[0][0]+=1
            elif a[0] == "L":
                T[0][0]-=1
            for j in range(9):
                if T[j+1][0] == T[j][0] and abs(T[j+1][1]-T[j][1]) > 1:
                    T[j+1][1] += 1 if T[j][1]-T[j+1][1] > 0 else -1
                elif T[j+1][1] == T[j][1] and abs(T[j+1][0]-T[j][0]) > 1:
                    T[j+1][0] += 1 if T[j][0]-T[j+1][0] > 0 else -1
                elif abs(T[j+1][0]-T[j][0]) > 1 or abs(T[j+1][1]-T[j][1]) > 1:
                    T[j+1][0] += 1 if T[j][0]-T[j+1][0] > 0 else -1
                    T[j+1][1] += 1 if T[j][1]-T[j+1][1] > 0 else -1
            S.append(str(T[9][0]) + "|" + str(T[9][1]))
    k = len(set(S))
    print("Part 2:",k)

part1()
part2()
