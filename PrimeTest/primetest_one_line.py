primetest = lambda n: n == 2 if n < 3 else n % 2 != 0 and [all((not (lambda a: pow(a, d, n) != 1 and not any(map(lambda i: pow(a, 2 ** i * d, n) == n - 1, range(s))))(random(2, n - 1)) for _ in range(N))) for s, d, random, N in [(*[list(iter(lambda: sd[1] % 2 == 1 or sd.__setitem__(0, sd[0] + 1) or sd.__setitem__(1, sd[1] // 2), True)) and False or sd for sd in [[0, n - 1]]][0], __import__("random").randint, 15)]][0]