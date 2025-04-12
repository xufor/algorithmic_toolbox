W, _ = list(map(int, input().split()))
w = list(map(int, input().split()))
dp = [[0 for _ in range(W + 1)] for _ in range(len(w) + 1)]

for i in range(1, len(w) + 1):
    for j in range(1, W + 1):
        if w[i - 1] > j:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j - w[i - 1]] + w[i - 1], dp[i - 1][j])

print(dp[-1][-1])
