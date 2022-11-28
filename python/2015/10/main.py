#!/usr/bin/env python3

import sys
sys.path.append("../../")
sys.path.append("../")
import util as u

###############
debug = False
###############

# file = "sample.txt" if debug else "input.txt"

def look_say(number, repeats):
    ret = []
    num = number
    for i in range(repeats):
        ret = []
        last = num[0]
        count = 1
        for a in num[1:]:
            if a == last:
                count+=1
            else:
                ret.append(count)
                ret.append(last)
                last = a
                count = 1
        ret.append(count)
        ret.append(last)
        num = ret
        # print(num)
    return ret

def read_input():
    return [1] if debug else [int(x) for x in "1113222113"]

def part1():
    A = read_input()
    k = len(look_say(A, 40))
    print("Part 1:",k)

def part2():
    A = read_input()
    k = len(look_say(A, 50))
    print("Part 2:",k)

part1()
part2()
