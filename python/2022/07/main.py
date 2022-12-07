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
    return u.read_lines(file)

def normalize(dir):
    dir = re.sub("//","/", dir)
    dir = re.sub("/[^\./]+/\.\./","/",dir)
    return dir


def init_tree(A):
    T = dict()
    t = []
    dir = ""
    read = False
    for a in A:
        if read:
            if a.startswith("$"):
                T[dir] = t
                read = False
            else: 
                t.append(a.split(" "))
                continue
        if a.startswith("$"):
            if a[2:].startswith("cd"):
                dir += "/"+a[5:]
                dir = normalize(dir)
            elif a[2:].startswith("ls"):
                read = True
                t = []
    T[dir] = t
    return T

dirs = dict()

def sum_dir(t, T):
    global dirs
    s = 0
    for k,v in T[t]:
        if k == "dir":
            vv = normalize(t+"/"+v)
            if v in dirs:
                s += dirs[vv]
            else:
                dirs[vv] = sum_dir(vv, T)
                s += dirs[vv]
        else:
            s += int(k)
    return s


def get_sum(T):
    global dirs
    dirs["/"] = sum_dir("/", T)
    

def print_tree(T, key, offset):
    root = T[key]
    print(" "*offset, key, "("+str(dirs[key])+")")
    for t in root:
        if t[0] == "dir":
            dir = normalize(key+"/"+t[1])
            print_tree(T, dir, offset+2)
        else:
            print(" "*(offset+2), t[1], t[0])

def part1():
    A = read_input()
    T = init_tree(A)
    get_sum(T)
    summ = 0
    for k in dirs:
        v = dirs[k]
        if v <= 100_000:
            summ += v
    # print_tree(T, "/", 0)
    print("Part 1:",summ)

def part2():
    A = read_input()
    T = init_tree(A)
    get_sum(T)
    total = 70_000_000 - dirs["/"]
    minn = 70_000_000
    for k in dirs:
        if total + dirs[k] >= 30_000_000 and minn > dirs[k]:
            minn = dirs[k]
    print("Part 2:",minn)

part1()
part2()
