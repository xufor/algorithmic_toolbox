str1 = input()
str2 = input()

dp = [[0 for _ in range(len(str1) + 1)] for _ in range(len(str2) + 1)]
for i in range(len(str2) + 1):
    for j in range(len(str1) + 1):
        if i == 0:
            dp[i][j] = j
        elif j == 0:
            dp[i][j] = i
        else:
            dp[i][j] = min(
                1 + dp[i - 1][j],
                1 + dp[i][j - 1],
                (0 if str1[j - 1] == str2[i - 1] else 1) + dp[i - 1][j-1]
            )

print(dp[-1][-1])