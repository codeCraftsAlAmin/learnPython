'''
1. Linear Search
Linear search is the simplest searching algorithm. It sequentially checks each element of the list until it finds the target value.
'''

def linear_search(arr, target):
    # print("arrgumnets: ",arr)
    # print("target: ",target)

    for i in arr:
        if i == target:
            return f"Target found"
    return "Target not found"

arr = [10,20,30,40,50]
target = 20

res = linear_search(arr, target)
print(res)
