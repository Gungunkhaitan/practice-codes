def merge_sort(arr):
    if len(arr)<=1:
        return arr
    else:
        mid=len(arr)//2
        left_arr=arr[:mid]
        right_arr=arr[mid:]
        left_arr = merge_sort(left_arr)
        right_arr = merge_sort(right_arr)
    return merge(left_arr,right_arr)

def merge(left,right):
    i=0
    j=0
    new=[]
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            new.append(left[i])
            i+=1
        else:
            new.append(right[j])
            j+=1
    new +=left[i:]
    new+=right[j:]
    return new

arr=[5,7,2,6,8,1,3]
print(merge_sort(arr))