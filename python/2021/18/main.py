#!/usr/bin/env python3

import sys
sys.path.append("../../")
import util as u

###############
debug = False
###############

file = "sample.txt" if debug else "input.txt"

def read_input():
    return u.read_lines(file)

def isNum(x):
    return x >= "0" and x <= "9"

def modify(l):
    res = []
    skip = -1
    for i,x in enumerate(list(l)):
        if i < skip:
            continue
        if x == "[" or x == "]":
            res.append(x)
        elif x == ",":
            pass
        elif isNum(x):
            j = i
            n = 0
            while isNum(l[j]):
                n *= 10
                n += int(l[j])
                j += 1
            res.append(n)
            skip = j
        else:
            pass
    return res

def add(A,B):
    res = ["["]
    res.extend(A)
    res.extend(B)
    res.append("]")
    return res

def split(l, i):
    k = l[i]
    a,b = k//2, ((k//2)+(k&1))
    l = l[:i]+["[",a,b,"]"]+l[i+1:]
#    printLine("split  > ",l)
    return False, l 

def explode(l, i):
    a,b = l[i+1],l[i+2]
    la = l[:i]
    lb = l[i+4:]
    for j in range(len(la)-1,-1,-1):
        if isinstance(la[j],int):
            la[j] += a
            break
    for j in range(len(lb)):
        if isinstance(lb[j],int):
            lb[j] += b
            break
    l = la + [0] + lb
#    printLine("explode> ",l)
    return False, l 

def reduce(l):
    while True:
        end = True
        depth = 0
        for i, x in enumerate(l):
            if x == "[":
                depth += 1
                if depth > 4:
                    end, l = explode(l, i)
                    break
            elif x == "]":
                depth -= 1
        if not end:
            continue
        for i, x in enumerate(l):
            if isinstance(x,int):
                if x > 9:
                    end, l = split(l, i)
                    break
        if end:
            return l

def printLine(p,l):
    if not debug:
        return
    out = []
    for i,x in enumerate(l):
        out.append(x)
        if i+1 == len(l):
            break
        if (isinstance(l[i],int) and (isinstance(l[i+1],int) or l[i+1] == "[")) or (l[i] == "]" and (l[i+1] == "[" or isinstance(l[i+1],int))):
            out.append(",")
        
    print(p,"".join([str(x) for x in out]))

def magnitude(l):
    if len(l) == 1:
        return l[0]
    else:
        depth = 0
        for i in range(len(l)):
            if l[i] == "[":
                depth += 1
            elif l[i] == "]":
                depth -= 1
            if depth == 1 and ((isinstance(l[i],int) and (isinstance(l[i+1],int) or l[i+1] == "[")) or (l[i] == "]" and (l[i+1] == "[" or isinstance(l[i+1],int)))):
                break
        return 3*magnitude(l[1:i+1]) + 2*magnitude(l[i+1:-1])


def part1():
    A = read_input()
    res = modify(A[0])
    for i in range(1, len(A)):
        res = add(res,modify(A[i]))
        res = reduce(res)
#        printLine("",res)
    k = magnitude(res)
    print("Part 1:",k)

def part2():
    A = read_input()
    B = [modify(a) for a in A]
    k = 0
    for i,b in enumerate(B):
        for j,bb in enumerate(B):
            if i != j:
                n = reduce(add(b,bb))
                r = magnitude(n)
#                print(r)
#                printLine("n",n)
#                printLine("b",b)
#                printLine("b",bb)
                if r > k:
                    k = r
    print("Part 2:",k)

part1()
part2()
