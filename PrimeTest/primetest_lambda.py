# try_comp = lambda a, d, n, s: pow(a, d, n) != 1 and not any(map(lambda i: pow(a, 2 ** i * d, n) == n - 1, range(s)))

# quorem = lambda n: [list(iter(lambda: sd[1] % 2 == 1 or sd.__setitem__(0, sd[0] + 1) or sd.__setitem__(1, sd[1] // 2),
#                               True)) and False or tuple(sd) for sd in [[0, n - 1]]][0]

primetest = lambda n: n == 2 if n < 3 else n % 2 != 0 and [all((not (lambda a: pow(a, d, n) != 1 and not any(map(lambda i: pow(a, 2 ** i * d, n) == n - 1, range(s))))(random(2, n - 1)) for _ in range(N))) for s, d, random, N in [(*[list(iter(lambda: sd[1] % 2 == 1 or sd.__setitem__(0, sd[0] + 1) or sd.__setitem__(1, sd[1] // 2), True)) and False or sd for sd in [[0, n - 1]]][0], __import__("random").randint, 15)]][0]

print(primetest(16826274250898468911280407749426542060694768486649616295792750595928899095760198861413145674011622196806001189975331140430984389138737798839798102100501250562384543970148324519320707086782480622768727739619400406298163697633506711667490859272493284358461677857576459592581649298303621108919528607436653031634208416252311924449922771895182310841019584155318547423916714195019363678142800559476884532645915293106647126449661258738488043253150745449466402688849719911594517744984668897073482226741417140010936686564467276499458185350171327208056715254738641774818774823242004784520937289671279357019604426730692283732729))
print(primetest(2938475483920938745789028764))
