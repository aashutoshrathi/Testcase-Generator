import math

pwr = math.pow
t = int(input())
while t > 0:
	a = int(input())
	sum = (a*(a+1))//2
	print((int(pwr(sum, 9))) % 1000000007)
	t -= 1
