input()
arr = list(map(int, input().split()))
input()
ques = list(map(int, input().split()))

def bin_search(arr, n, i = 0, j = len(arr)-1):
    if i <= j:
        mid = i + (j - i) // 2
        if arr[mid] == n:
            return mid
        elif arr[mid] > n:
            return bin_search(arr, n, i, mid - 1)
        else:
            return bin_search(arr, n, mid + 1, j) 
    else:
        return -1
    
for q in ques:
    print(bin_search(arr, q), end=" ")
print()