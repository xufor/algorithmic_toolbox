input()
nums = list(map(int, input().split()))

total_of_nums = sum(nums)
if len(nums) < 3 or total_of_nums % 3 != 0 or max(nums) > total_of_nums // 3:
    print(0)
else:
    one_third = total_of_nums // 3
    dp = [[[False for _ in range(one_third + 1)] for _ in range(one_third + 1)] for _ in range(len(nums) + 1)]
    dp[0][0][0] = True

    for i in range(1, len(nums) + 1):
        for j in range(one_third + 1):
            for k in range(one_third + 1):
                if j == 0 and k == 0:
                    dp[i][0][0] = True
                else:
                    ith_element = nums[i - 1]
                    #trying to put ith elemet in 1st bucket
                    if ith_element > j:
                        ans1 = dp[i - 1][j][k]
                    else:
                        ans1 = dp[i - 1][j - ith_element][k]
                    #trying to put ith elemet in 2nd bucket
                    if ith_element > k:
                        ans2 = dp[i - 1][j][k]
                    else:
                        ans2 = dp[i - 1][j][k - ith_element]
                    dp[i][j][k] = ans1 or ans2
    print(1 if dp[-1][-1][-1] else 0)