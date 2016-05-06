def lcm(a, b):
	product = a*b

	while b>0:
		tmp = b
		b = a%b
		a = tmp

	return product/a

def multiply_lcm(n):
	return reduce(lcm, xrange(1, n+1))

# print lcm(17, 3)
print multiply_lcm(5)

def primes_less_than(n):
	prime_list = [2,3,5,7,11,13,17,19]
	return prime_list

def multiply_lcm(n):
	product = 1

	for p in primes_less_than(n):
		x = 1
		while x*p<=n:
			x=x*p

		product = product*x

	return product

print multiply_lcm(5)