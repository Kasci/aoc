import re

def parse(l):
    if "NOT" in l:
        return ("not", l[4:])
    elif "AND" in l:
        n = l.split(" ")
        return ("and", n[0], n[2])
    elif "OR" in l:
        n = l.split(" ")
        return ("or", n[0], n[2])
    elif "LSHIFT" in l:
        n = l.split(" ")
        return ("lshift", n[0], n[2])
    elif "RSHIFT" in l:
        n = l.split(" ")
        return ("rshift", n[0], n[2])
    else:
        return ("value", l)

def build(list):
    d = dict()
    for l in list:
        d[l[1]] = parse(l[0])
    return d

def execute(d, v, l):
    if l in v:
        return v[l]
    a = d[l]
    # print(l, a)
    ret = 0
    if a[0] == "value":
        ret = execute(d, v, a[1]) if re.match("[a-z]+", a[1]) else int(a[1])
    elif a[0] == "or":
        _x = execute(d, v, a[1]) if re.match("[a-z]+", a[1]) else int(a[1])
        _y = execute(d, v, a[2]) if re.match("[a-z]+", a[2]) else int(a[2])
        ret = _x | _y
    elif a[0] == "and":
        _x = execute(d, v, a[1]) if re.match("[a-z]+", a[1]) else int(a[1])
        _y = execute(d, v, a[2]) if re.match("[a-z]+", a[2]) else int(a[2])
        ret = _x & _y
    elif a[0] == "lshift":
        _x = execute(d, v, a[1]) if re.match("[a-z]+", a[1]) else int(a[1])
        _y = execute(d, v, a[2]) if re.match("[a-z]+", a[2]) else int(a[2])
        ret = _x << _y
    elif a[0] == "rshift":
        _x = execute(d, v, a[1]) if re.match("[a-z]+", a[1]) else int(a[1])
        _y = execute(d, v, a[2]) if re.match("[a-z]+", a[2]) else int(a[2])
        ret = _x >> _y
    elif a[0] == "not":
        ret = ~(execute(d, v, a[1]) if re.match("[a-z]+", a[1]) else int(a[1]))
    v[l] = ret & 0xffff
    return ret & 0xffff
        