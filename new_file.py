def search(arr, low, high, target):
    if low <= target:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            return search(arr, mid + 1, high, target)
        else:
            return search(arr, low, mid - 1, target)
        
    else:
        return -1


arr = [ 2, 3, 4, 10, 40 ]
target = 100
low = 0
high = len(arr) - 1

res = search(arr, low, high, target)

if res != -1:
    print("Element found at index no: ", res)
else:
    print("Element is not present in array")