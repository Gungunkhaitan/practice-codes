arr=[1,4,2,3,10,9,6,8,7]
n=len(arr)
for i in range(n-1):
    min_idx=i
    for j in range(i+1,n):
        if arr[min_idx]>arr[j]:
            min_idx=j
    arr[i],arr[min_idx] = arr[min_idx], arr[i]
print(arr)