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
    return [a.split(" ") for a in u.read_lines(file)]

def use(t, ls, Y):
    l = t.split("?")[0]
    n = [i for i in l.split(".") if len(i) > 0]
    if len(n) == 0 or \
        (len(n) <= len(ls) and \
            (all([len(n[i]) == ls[i] for i in range(len(n))]) or \
                (all([len(n[i]) == ls[i] for i in range(len(n)-1)]) and len(n[len(n)-1]) < ls[len(n)-1]))):
        Y.append(t)


def work(L,R):
    ls = [int(i) for i in R.split(",")]
    k = 0
    X = [L]
    for i in range(len(L)):
        if L[i] == "?":
            Y = [] 
            for x in X:
                use(x[:i]+"#"+x[i+1:], ls, Y)
                use(x[:i]+"."+x[i+1:], ls, Y)
            X = Y
            # print(Y)
    o = 1
    for x in X:
        n = [i for i in x.split(".") if len(i) > 0]
        if len(ls) != len(n):
            continue
        q = 1 if all([len(n[i]) == ls[i] for i in range(len(n))]) else 0
        # if q == 1:
        #     print("%5d %s" % (o, "".join([x[m] if L[m] == "?" else "X" if L[m] == "#" else "_" for m in range(len(L))])))
        #     o += 1
        k += q
    return k

def part1():
    A = read_input()
    k = 0
    for a in A:
        k += work(a[0], a[1])
    print("Part 1:",k)


def part2():
    A = read_input()
    k = 0
    i = 1
    for a in A:
        na = work(a[0], a[1])
        two = work(a[0]+"?"+a[0], a[1]+","+a[1])
        three = work(a[0]+"?"+a[0]+"?"+a[0], a[1]+","+a[1]+","+a[1])
        dif = two/na
        diff = three/two
        print("%4d %5d %5d %5d %03.3f %03.3f" % (i, na, two, three, dif, diff))
        i += 1
        k += na * (dif**4)
    print("Part 2:",k)

# part1()
part2()
