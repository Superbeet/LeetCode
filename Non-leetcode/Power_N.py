def power(x, n):
	print n

	if n==0:
		return 1.0

	if n==-1:
		return float(1)/x

	if n==1:
		return float(x)

	if abs(x)<0.001:
		return 0.0

	half = power(x, n/2)

	if n%2==0:
		return half*half
	elif n>0:
		return half*half*x
	else:
		return half*half/x

# print power(2,10)
# print power(2, 1)
print power(8, -2)
# print power(2,-1)