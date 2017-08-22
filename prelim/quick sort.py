def quick_sort(arr):
    if len(arr) < 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right  = [x for x in arr if x > pivot]

    return quick_sort(left) +middle+ quick_sort(right)

print(quick_sort([3,6,8,10,90,2,1]))
