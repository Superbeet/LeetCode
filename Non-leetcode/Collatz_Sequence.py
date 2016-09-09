cache = {1: 1}

def collatz_cache(n):
    path = [n]
    while n not in cache:
        if n % 2:
            n = 3 * n + 1
        else:
            n = n / 2
        path.append(n)

    for i, m in enumerate(reversed(path)):
        cache[m] = cache[n] + i

def collatz_calculate(n):
    
    path = [n]

    while n not in cache:
        if n % 2 == 0:
            n /= 2
        else:
            n = 3*n + 1
        path.append(n)

    for i, m in enumerate(reversed(path))
        cache[m] = cache[n] + i

    return cache[path[0]]