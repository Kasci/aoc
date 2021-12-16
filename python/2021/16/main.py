#!/usr/bin/env python3

import sys
sys.path.append("../../")
import util as u
from functools import reduce
import operator

###############
debug = False 
###############

file = "sample.txt" if debug else "input.txt"
part = 1

S = []

def read_input():
    return u.read_lines(file)

def lprint(*s):
    if debug:
        print(s)

def parse_literal(n):
    lprint("lit> ",n)
    k = 0
    while True:
        if len(n) < 5:
            return 0, None
        p = n[0:5]
        k = (k << 4) + int(p[1:],base=2)
        n = n[5:]
        if p[0] == "0":
            break
    return k, n

def parse_operand(n):
    if n == None or len(n) < 12:
        return 0, None
    i = n[0]
    n = n[1:]
    lprint("ope> ",i,n)
    v = 0
    if i == "0":
        L = int(n[:15],base=2)
        n = n[15:]
        lprint("op0> ",L,n)
        l = len(n) - L
        while n != None and l != len(n) and len(n) > 0:
            lprint("bn0> %d %d"%(l, -1 if n == None else len(n)))
            vv, n = parse_token(n)
            lprint("in0> %d"% -1 if n == None else len(n))
            v += vv
        lprint("rop0")
    else:
        L = int(n[:11],base=2)
        n = n[11:]
        lprint("op1> ",L,n)
        for it in range(L):
            if n == None or len(n) <= 0:
                break
            vv, n = parse_token(n)
            lprint("in1> %d %d"% (it,-1 if n == None else len(n)))
            v += vv
        lprint("rop1")
    lprint("rop> ",v,n)
    return v, n

def add_end_function_to_stack(s):
    global S
    S.append(
        "_add" if s == 0 else
        "_product" if s == 1 else
        "_min" if s == 2 else 
        "_max" if s == 3 else 
        "_gt" if s == 5 else 
        "_lt" if s == 6 else
        "_eq" if s == 7 else 
        "???"
    )

def add_function_to_stack(s):
    global S
    S.append(
        "add" if s == 0 else
        "product" if s == 1 else
        "min" if s == 2 else 
        "max" if s == 3 else 
        "gt" if s == 5 else 
        "lt" if s == 6 else
        "eq" if s == 7 else 
        "???"
    )

def add_to_stack(s):
    global S
    S.append(s)

def parse_token(n):
    global part
    if part == 1:
        return parse_token1(n)
    else:
        return parse_token2(n)

def parse_token1(n):
    if n == None or len(n) < 6:
        return 0, None 
    v = int(n[0:3],base=2)
    t = int(n[3:6],base=2)
    b = n[6:]
    lprint("tok> ",v,t,b)
    if t == 4:
        k, nn = parse_literal(b)
    else:
        vv, nn = parse_operand(b)
        v += vv
    lprint("rtk> ", v, nn)
    return v, nn

def parse_token2(n):
    if n == None or len(n) < 6:
        return 0, None 
    v = int(n[0:3],base=2)
    t = int(n[3:6],base=2)
    b = n[6:]
    lprint("tok> ",v,t,b)
    if t == 4:
        k, nn = parse_literal(b)
        add_to_stack(k)
    else:
        add_function_to_stack(t)
        vv, nn = parse_operand(b)
        add_end_function_to_stack(t)
        v += vv
    lprint("rtk> ", v, nn)
    return v, nn

def eval_stack(n):
    global S
    task = S[n]
    n += 1
    v = []
    while isinstance(S[n],int) or S[n][0] != "_":
        if isinstance(S[n],int):
            v.append(S[n])
            n += 1
        else:
            n, k = eval_stack(n)
            v.append(k)
    n += 1
    if task == "add":
        return n, sum(v)
    elif task == "product":
        return n, reduce(operator.mul, v, 1) 
    elif task == "min":
        return n, min(v)
    elif task == "max":
        return n, max(v)
    elif task == "lt":
        return n, 1 if v[0] < v[1] else 0
    elif task == "gt":
        return n, 1 if v[0] > v[1] else 0
    elif task == "eq":
        return n, 1 if v[0] == v[1] else 0
    else:
        raise Exception("Unreachable")


def part1():
    A = read_input()
    k = 0
    for a in A:
        n = "".join(["{:04b}".format(int(x,base=16)) for x in list(a)])
        k, nn = parse_token(n)
        if not debug:
            break
    print("Part 1:",k)

def part2():
    A = read_input()
    k = 0
    for a in A:
        n = "".join(["{:04b}".format(int(x,base=16)) for x in list(a)])
        g, nn = parse_token(n)
        if not debug:
            break
    n, k = eval_stack(0)
    print("Part 2:",k)

part1()
part=2
part2()
