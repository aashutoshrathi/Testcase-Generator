import math

pwr = math.pow
t = int(input())
while t > 0:
	a = int(input())
	#sum = (a*(a+1))//2
	sum=a+a
	print(sum)
	#print((int(pwr(sum, 2))) % 1000000007)
	t -= 1
