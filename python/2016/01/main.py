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
    return u.read_lines(file)[0].split(", ")

def part1():
    A = read_input()
    k = 0
    f = 0
    x,y = 0,0
    for a in A:
        if a[0] == "R":
            f += 1
            f %= 4
        else:
            f -= 1
            f = (f+4)%4
        if f == 0:
            y -= int(a[1:])
        elif f == 2:
            y += int(a[1:])
        elif f == 1:
            x += int(a[1:])
        else:
            x -= int(a[1:])
        k = abs(x) + abs(y)
    print("Part 1:",k)

def part2():
    A = read_input()
    k = -1
    f = 0
    N = 1000
    lx,ly = N,N

    x,y = 0,0
    q = [[0 for _ in range(2*N)] for _ in range(2*N)]
    for a in A:
        n = int(a[1:])
        if a[0] == "R":
            f += 1
            f %= 4
        else:
            f -= 1
            f = (f+4)%4
        x = lx + (n if f == 1 else -1*n if f == 3 else 0)
        y = ly + (n if f == 2 else -1*n if f == 0 else 0)
        if f in [1,3]:
            for i in range(x,lx,1 if x<lx else -1):
                if q[y][i] == 1:
                    k = abs(y-N) + abs(i-N)
                    break 
                q[y][i] = 1
        else:
            for i in range(y,ly,1 if y<ly else -1):
                if q[i][x] == 1:
                    k = abs(x-N) + abs(i-N)
                    break
                q[i][x] = 1
        if k > 0:
            break
        lx,ly = x,y
    print("Part 2:",k)


part1()
part2()
