def find_next_prime(n):
    return find_prime_in_range(n, 2*n)

def find_prime_in_range(a, b):
    for j in range(a, b):
        for i in range(2, j):
			if j % i == 0:
				break
			else:
				return i
    return None

if __name__ == '__main__':
    n = input('Find the next prime number greater great than: ')
    print find_next_prime(n+1)