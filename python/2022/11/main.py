#!/usr/bin/env python3

import sys
sys.path.append("../../")
sys.path.append("../")
import util as u
import re

###############
debug = False
###############

file = "sample.txt" if debug else "input.txt"

def read_input():
    X = u.read_lines(file)
    A = []
    for i in range((len(X)+1)//7):
        a = dict()
        for j in range(7):
            if i*7+j >= len(X):
                break
            x = X[i*7+j]
            if j == 1:
                m = re.match(".*Starting items: (.*)", x).group(1)
                a['items'] = [int(n) for n in m.split(",")]
            elif j == 2:
                m = re.match(".*Operation: new = (.*)", x).group(1)
                a['operation'] = m.split(" ")
            elif j == 3:
                m = re.match(".*Test: divisible by (.*)", x).group(1)
                a['test'] = int(m)
            elif j == 4:
                m = re.match(".*If true: throw to monkey (.*)", x).group(1)
                a['true'] = int(m)
            elif j == 5:
                m = re.match(".*If false: throw to monkey (.*)", x).group(1)
                a['false'] = int(m)
            a['check'] = 0
        A.append(a)
    return A

def calc(val, op):
    if op[1] == "*":
        return (val if op[0] == "old" else int(op[0])) * (val if op[2] == "old" else int(op[2]))
    else:
        return (val if op[0] == "old" else int(op[0])) + (val if op[2] == "old" else int(op[2]))

def part1():
    A = read_input()
    for _ in range(20):
        for a in A:
            a['items'].reverse()
            b = a['items']
            while len(b) > 0:
                val = b.pop()
                new_val = calc(val, a['operation'])
                new_val = new_val // 3 
                a['check'] += 1
                if new_val % a['test'] == 0:
                    A[a['true']]['items'].append(new_val)
                else:
                    A[a['false']]['items'].append(new_val)
    N = sorted([a['check'] for a in A], reverse=True)
    k = N[0]*N[1]
    print("Part 1:",k)

def get_mod(A):
    r = 1
    for a in A:
        r *= a 
    return r

def part2():
    A = read_input()
    Q = get_mod([a['test'] for a in A])
    for j in range(10000):
        for a in A:
            a['items'].reverse()
            b = a['items']
            while len(b) > 0:
                val = b.pop()
                new_val = calc(val, a['operation'])
                new_val = new_val % Q
                a['check'] += 1
                if new_val % a['test'] == 0:
                    A[a['true']]['items'].append(new_val)
                else:
                    A[a['false']]['items'].append(new_val)
    N = sorted([a['check'] for a in A], reverse=True)
    k = N[0]*N[1]
    print("Part 2:",k)

part1()
part2()
