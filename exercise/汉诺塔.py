# -*- coding: utf-8 -*-
def move(n, a, b, c):
	if n == 1:
		print(a, '-->', c)
	else:
		move(n-1, a, c, b)
		print(a, '-->', c)
		move(n-1, b, a, c)
n = int(input('输入n'))
a = input('输入A')
b = input('输入B')
c = input('输入C')
move(n, a, b, c)