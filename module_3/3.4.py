n = int(input())
profits = list(map(int, input().split()))
clicks = list(map(int, input().split()))

profits.sort()
clicks.sort()
final_value = 0
for (p, c) in zip(profits, clicks):
    final_value += p * c
print(final_value)