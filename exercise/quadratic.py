import math
def quadratic(a,b,c):
	delta = b*b-4*a*c
	if delta < 0:
		return 'False'
	elif delta == 0:
		return -b/(2*a)
	else:
		return (-b+math.sqrt(delta))/(2*a) , (-b-math.sqrt(delta))/(2*a)
a = float(input('输入参数a'))
b = float(input('输入参数b'))
c = float(input('输入参数c'))
print(quadratic(a,b,c))