input()
arr = list(map(int, input().split()))
input()
ques = list(map(int, input().split()))

result = -1
def bin_search(arr, n, i = 0, j = len(arr)-1):
    global result
    if i <= j:
        mid = i + (j - i) // 2
        if arr[mid] == n:
            result = mid
            bin_search(arr, n, i, mid - 1)
        elif arr[mid] > n:
            bin_search(arr, n, i, mid - 1)
        else:
            bin_search(arr, n, mid + 1, j) 
    
for q in ques:
    result = -1
    bin_search(arr, q)
    print(result, end=" ")
print()