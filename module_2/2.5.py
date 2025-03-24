n, m = map(int, input().split())

if n <= 1:
    print(n)
else:
    mod_series = [0, 1]
    a, b = 0, 1
    while True:
        c = a + b
        a = b
        b = c
        if c % m == 0 and (a + b) % m == 1:
            break
        mod_series.append(c % m)
    print(mod_series[ n % len(mod_series)])

        
