m, n = map(int, input().split())

def fib_mod(n, m):
    if n <= 1:
        return(n)
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
        return mod_series[n % len(mod_series)]

fib_mod_10_of_n_plus_2 = fib_mod(n+2, 10)
fib_mod_10_of_m_plus_1 = fib_mod(m+1, 10)
diff = fib_mod_10_of_n_plus_2 - fib_mod_10_of_m_plus_1
print(10 + diff if diff < 0 else diff)