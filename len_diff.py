# https://www.codewars.com/kata/5663f5305102699bad000056/train/python


def mxdiflg(a1, a2):
    if len(a1) == 0 or len(a2) == 0:
        return -1
    MAX = 0
    for string1 in a1:
        for string2 in a2:
            NUM = abs(len(string1) - len(string2))
            if NUM > MAX:
                MAX = NUM
    return MAX