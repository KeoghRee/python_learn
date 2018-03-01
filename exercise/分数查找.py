# -*- coding: utf-8 -*-
namelist = ['John','Mike','Alice']
score = [87,98,98]
name= input('请输入名字')
n = 0
s = 0
while n < len(namelist):
	if name != namelist[n]:
		n=n+1
		continue
	s = str(score[n])
	print(name+'的分数是'+s)
	break
if s == 0:
	print('Can not find')