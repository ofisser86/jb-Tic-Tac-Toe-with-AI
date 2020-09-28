prime_numbers = [n for n in range(2, 1001) if all(n % i != 0 for i in range(2, n - 1))]

