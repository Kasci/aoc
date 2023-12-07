#!/usr/bin/env python3

import sys
sys.path.append("../../")
sys.path.append("../")
import util as u

###############
debug = False
###############

file = "sample.txt" if debug else "input.txt"

# D = dict()

def read_input():
    X = u.read_lines(file)
    s = [int(x) for x in X[0].split(" ")[1:]]
    m = [[[int(w) for w in q.split(" ")] for q in t[1:]] for t in [x.split("\n") for x in "\n".join(X[2:]).split("\n\n")]]
    return (s,m)

def calc(s,M):
    # if s in D:
    #     return D[s]
    t = s
    for i,m in enumerate(M):
        for r in m:
            if t >= r[1] and t < r[1]+r[2]:
                t = r[0]+t-r[1]
                break
    # if s not in D:
    #     D[s] = t
    return t

def part1():
    S,M = read_input()
    k = 99999999999
    for s in S:
        # print("s",s)
        t = calc(s,M)
        #     print(t)
        # print("---")
        if t < k:
            k = t
    print("Part 1:",k)

def part2():
    S,M = read_input()
    k = 99999999999
    for i in range(len(S)//2):
        print(i, len(S)//2)
        for s in range(S[2*i], S[2*i]+S[2*i+1]):
            t = calc(s,M)
            if t < k:
                k = t
    print("Part 2:",k)

print("""
      ----------------------
      This is not optimal solution, part 2 takes hours,
      But it finishes and calculates correctly.
      ----------------------
""")
part1()
part2()
