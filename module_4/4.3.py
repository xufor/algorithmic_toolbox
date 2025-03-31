input()
arr = list(map(int, input().split()))

candidate, count = None, 1

for n in arr:
    if n == candidate:
        count += 1
    else:
        count -= 1
    if count == 0:
        count = 1
        candidate = n

actual_count = 0
for n in arr:
    if n == candidate:
        actual_count += 1

if actual_count > (len(arr) / 2):
    print(1)
else:
    print(0)