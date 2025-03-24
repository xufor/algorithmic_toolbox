from functools import cmp_to_key

n = int(input())
numbers = list(input().split())
numbers.sort(key=cmp_to_key(lambda a,b: -1 if (a+b) < (b+a) else 1), reverse=True)
print("".join(numbers))