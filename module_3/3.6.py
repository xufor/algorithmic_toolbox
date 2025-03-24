n = int(input())

count_of_numbers = 1
while True:
    lhs = (count_of_numbers + 1)*(count_of_numbers)
    rhs = 2 * n
    if lhs >= rhs:
        if lhs > rhs:
            count_of_numbers -= 1
        break
    count_of_numbers += 1
print(count_of_numbers)
delta = n - int((count_of_numbers * (count_of_numbers + 1)) / 2)
for i in range(1, count_of_numbers + 1):
    print(i if i != count_of_numbers else i + delta, end=" ")
print()
