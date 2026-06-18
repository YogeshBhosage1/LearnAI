def unique_prime_factors(n):
    factors = []

    if n % 2 == 0:
        factors.append(2)
        while n % 2 == 0:
            n //= 2

    d = 3
    while d * d <= n:
        if n % d == 0:
            factors.append(d)
            while n % d == 0:
                n //= d
        d += 2

    if n > 1:
        factors.append(n)

    return factors


if __name__ == "__main__":
    print(unique_prime_factors(12))   # [2, 3]
    print(unique_prime_factors(100))  # [2, 5]
    print(unique_prime_factors(315))  # [3, 5, 7]
