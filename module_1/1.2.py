input()
nums = [n for n in map(int, input().split())]
l, sl = max(nums[0], nums[1]), min(nums[0], nums[1])
for i in range(2, len(nums)):
    if nums[i] > l:
        sl = l
        l = nums[i]
    elif nums[i] > sl:
        sl = nums[i]
print(l * sl)