amt = int(input())
dp = [0 for _ in range(amt + 1)]
dp[0] = 0
for i in range(1, amt + 1):
    handle_invalid_index = lambda x: dp[x] if x >= 0 else 10**9
    dp[i] = 1 + min(
        handle_invalid_index(i - 1),
        handle_invalid_index(i - 3),
        handle_invalid_index(i - 4),
    )
print(dp[-1])
