l = [1, 3, 5, 5, 6, 8, 9]
index = {}

for i, num in enumerate(sorted(set(l))):
	index[num] = i + 1

print [index[num] for num in l]
