n = int(input())
dp = [0 for _ in range(n + 1)]
dp[1] = 0
for i in range(2, n + 1):
    dp[i] = 1 + min(
        dp[i - 1],
        dp[i // 2] if i % 2 == 0 else 10**9,
        dp[i // 3] if i % 3 == 0 else 10**9
    )

print(dp[-1])

k = n
seq = [k]
while k > 1:
    next_k = k - 1
    if k % 2 == 0 and dp[k // 2] < dp[next_k]:
        next_k = k // 2
    if k % 3 == 0 and dp[k // 3] < dp[next_k]:
        next_k = k // 3
    k = next_k
    seq.append(next_k)
seq.reverse()

for val in seq:
    print(val, end=" ")
print()