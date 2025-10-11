'''
Interpolation search is an improved version of binary search, especially suitable for large and uniformly distributed arrays. It calculates the probable position of the target value based on the value of the key and the range of the search space.
'''

def search(arr, low, high, target):
    while low <= high and arr[low] <= target and arr[high] >= target:
        pos = low + ((high - low) // (arr[high] - arr[low])) * (target - arr[low])

        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = low + 1
        else:
            high = high + 1

    return -1

arr = [2, 3, 4, 10, 40]
target = 3

low = 0
high = len(arr) - 1

res = search(arr, low, high, target)

if res != -1:
    print("Element found at index no:", res)
else:
    print("Element not found")