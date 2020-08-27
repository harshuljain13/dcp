def get_right_elements(arr):

    def recursion(start, end):
        if start>end:
            return
        if start==end:
            return [arr[start]]
        mid = start+(end-start)//2
        left_arr = recursion(start, mid)
        right_arr = recursion(mid+1, end)
        sorted_arr = merge(left_arr, right_arr, start, end)
        return sorted_arr

    def merge(left_arr, right_arr, start, end):
        i = 0
        j = 0
        sorted_arr = []
        while i<len(left_arr) and j<len(right_arr):
            if left_arr[i] <= right_arr[j]:
                sorted_arr.append(left_arr[i])
                res_arr[start+i]+=j
                i+=1
            else:
                sorted_arr.append(right_arr[j])

                
                j+=1

        while i<len(left_arr):
            sorted_arr.append(left_arr[i])
            res_arr[start+i]+=j
            i+=1
        while j<len(right_arr):
            sorted_arr.append(right_arr[j])
            j+=1
        return sorted_arr

    res_arr = [0]*len(arr)
    recursion(0, len(arr)-1)
    return res_arr

arr = [1,6,9,4,2,1]
print(get_right_elements(arr))