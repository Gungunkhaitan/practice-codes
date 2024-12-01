def quicksort(arr,left,right):
    if left<right:
        pivot_pos=partition(arr,left,right)
        quicksort(arr,left,pivot_pos-1)
        quicksort(arr,pivot_pos+1,right)

def partition(arr,left,right):
    i=left
    j=right-1
    pivot=arr[left]
    while i<j:
        while arr[i]<pivot and i <right:
            i+=1
        while arr[j]>pivot and j>left:
            j-=1
        
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
    if arr[i]>pivot:
        arr[i],arr[left]=arr[left],arr[i]
    return i

arr=[15,20,35,3,41,47]
quicksort(arr,0,len(arr)-1)
print(arr)