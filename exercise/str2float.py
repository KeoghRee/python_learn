# -*- coding: utf-8 -*-
from functools import reduce

def str2float(s):
	m = 0
    for k in s:
        if k =='.':
            break
        else: m = m+1
    s = s[:m]+s[m+1:]
    m = len(s) - m
    L = {'1':1, '2': 2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '0':0}
    n = map(lambda x: L[x], s)
    return reduce(lambda x, y: 10*x+y , n)/(10**m)