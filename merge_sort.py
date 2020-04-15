#DIVIDE
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    # split my array in half
    middle = len(arr) // 2
    left = arr[:middle]
    right = arr[middle:]
# split each of those halves in half - RECURSIVE?  BASE CASE?
    left_arr = merge_sort(left)
    right_arr = merge_sort(right)
# keep going until there is one number left
    return merge(left_arr, right_arr)

#JOIN
def merge(left, right):
    # join the two halves back together in a sorted manner
    joined_arr = []
    # create three pointers to track location in arrs
    i = j = k = 0

    while i < len(left) and j < len(left):
        if left[i] <= right[j]:
            joined_arr.append(left[i])
            i += 1
        else:
            joined_arr.append(right[j])
            j += 1
        k += 1

    if i < len(left):
        joined_arr += left[i:]

    if j < len(right):
        joined_arr += right[j:]

    return joined_arr

print(merge_sort([1,6,5,3,2,5,7,7, 0, 0, -3, -5]))