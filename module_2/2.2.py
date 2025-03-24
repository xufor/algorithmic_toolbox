n = int(input())

if n <= 1:
    print(n)
else:
    a_ld, b_ld = 0, 1
    for i in range(2, n+1):
        c_ld = (a_ld + b_ld) % 10
        a_ld = b_ld
        b_ld = c_ld
    print(b_ld)
# 0 1 1 2 3 5 8 13 21 34