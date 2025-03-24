n = int(input())

if n <= 2:
    print(n)
else:
    mod_series = [0, 1]
    a, b = 0, 1
    while True:
        c = a + b
        a = b
        b = c
        if c % 10 == 0 and (a + b) % 10 == 1:
            break
        mod_series.append(c % 10)
    mod_fib_n_plus_2 = mod_series[ (n + 2) % len(mod_series)]
    print(mod_fib_n_plus_2 - 1 if mod_fib_n_plus_2 > 0 else 9)
