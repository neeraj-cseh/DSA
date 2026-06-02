def factors(num):
    n = num
    factors = []
    for i in range(1, n // 2 + 1):
        if n % i == 0:\
            factors.append(i)
    factors.append(n)
    print(factors)
factors(12)