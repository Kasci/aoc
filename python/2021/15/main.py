#!/usr/bin/env python3

import sys
sys.path.append("../../")
import util as u

###############
debug = False
###############

file = "sample.txt" if debug else "input.txt"

def read_input():
    return [[int(x) for x in a] for a in u.read_lines(file)]

def reconstruct(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    return path[-2::-1]

def a_star(start, end, A):
    maxY, maxX = len(A), len(A[0])
    open_set = set()
    open_set.add(start)
    came_from = {}
    g_score = dict() 
    for y in range(len(A)):
        for x in range(len(A[0])):
            g_score[(x,y)] = 2**100
    g_score[start] = 0
    f_score = dict()
    for y in range(len(A)):
        for x in range(len(A[0])):
            f_score[(x,y)] = 2**100
    f_score[start] = A[start[1]][start[0]]
    while len(open_set) > 0 :
        score_set = [x for x in list(open_set)]
        current = sorted(score_set, key=lambda x: f_score[x])[0]
        if current == end:
            return reconstruct(came_from, current)
        open_set.remove(current)
        x,y = current
        up = (x,y-1) if y-1 >= 0    else None
        dn = (x,y+1) if y+1 <  maxY else None
        lf = (x-1,y) if x-1 >= 0    else None
        rg = (x+1,y) if x+1 <  maxX else None
        gg_score = g_score[current] + 1
        ff_score = f_score[current] + A[y][x]
        for n in [up,dn,lf,rg]:
            if n == None:
                continue
            if ff_score < f_score[n]:
                came_from[n] = current
                g_score[n] = gg_score
                xx,yy = n
                f_score[n] = ff_score
                if n not in open_set:
                    open_set.add(n)
    return None


def part1():
    A = read_input()
    N = a_star((0,0), (len(A[0])-1,len(A)-1), A)
    k = sum([A[y][x] for x,y in N])
    print("Part 1:",k)

def part2():
    A = read_input()
    v = lambda x : x if x < 10 else x-9
    B = [[v(A[y%len(A)][x%len(A[0])]+(x//len(A[0])+y//len(A))) for x in range(len(A[0])*5)] for y in range(len(A)*5)]
    N = a_star((0,0), (len(B[0])-1,len(B)-1), B)
    k = sum([B[y][x] for x,y in N])
    print("Part 2:",k)

part1()
part2()
