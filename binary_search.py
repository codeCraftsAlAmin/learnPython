'''
# # Binary Search
Binary search is a more efficient searching algorithm suitable for sorted lists. It repeatedly divides the search interval in half until the target value is found.
'''

def search(arr, low, high, target):

    if low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        
        elif arr[mid] < target:
            return search(arr, mid+1, high, target)
        else:
             return search(arr, low, mid-1, target)
    
    else:
        return - 1


arr = [ 2, 3, 4, 10, 40 ]
target = 40

low = 0

high = len(arr)-1

res = search(arr, low, high, target)


if res != -1:
    print("Element is present at index: ", str(res))

else:
    print("Not found")

print("Operation finished")