def count_array_inversions(arr, low, high):
    if high==low:
        return 0, [arr[low]]

    mid = low+(high-low)//2
    left_count, left_sorted_array = count_array_inversions(arr, low, mid)
    right_count, right_sorted_array = count_array_inversions(arr, mid+1, high)
    merge_count, sorted_array = merge_arrays(left_sorted_array, right_sorted_array)

    return left_count+right_count+merge_count, sorted_array

def merge_arrays(arr1, arr2):
    count = 0
    n = len(arr2)
    m = len(arr1)

    i = 0
    j = 0
    new_array = []
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<arr2[j]:
            new_array.append(arr1[i])
            i+=1
        else:
            count+=len(arr1)-i
            new_array.append(arr2[j])
            j+=1

    while i<len(arr1):
        new_array.append(arr1[i])
        i+=1

    while j<len(arr2):
        new_array.append(arr2[j])
        j+=1
    return count, new_array

arr = [5,4,3,2,1]
print(count_array_inversions(arr, 0, len(arr)-1)[0])