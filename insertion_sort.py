arr=[5,7,2,6,8,1,3]
n=len(arr)

for i in range(1,n):
    key=arr[i]
    j=i-1
    while j>=0 and key<arr[j]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
        j=j-1
    arr[j+1]=key
print(arr)
        