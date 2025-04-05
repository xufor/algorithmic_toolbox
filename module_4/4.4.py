import random
input()
arr = list(map(int, input().split()))

def partition(arr, low, high):
    pivot_index = random.randint(low, high)
    pivot = arr[pivot_index]
    arr[pivot_index], arr[low] = arr[low], arr[pivot_index]
    i = low

    for j in range(low + 1, high + 1):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i], arr[low] = arr[low], arr[i]
    p1 = i

    i = p1
    for j in range(p1 + 1, high + 1):
        if arr[j] == arr[p1]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    p2 = i

    return p1, p2


def quicksort(arr, low, high):
    if low < high:
        p1, p2 = partition(arr, low, high)
        quicksort(arr, low, p1 - 1)
        quicksort(arr, p2 + 1, high)

quicksort(arr, 0, len(arr) - 1)
for i in range(len(arr)):
    print(arr[i], end=" ")
print()
