'''
Jump search is another searching algorithm suitable for sorted arrays. It jumps ahead by a fixed number of steps and then performs a linear search in the smaller range.
'''
from math import sqrt

def search(arr, target):

    n = len(arr)
    step = int(sqrt(n))
    prev = 0

    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(sqrt(n))

        if prev >= n:
            return - 1
    while arr[prev] < target:
        prev += 1

        if prev == min(step,n):
            return - 1
    
    if arr[prev] == target:
        return prev
    return - 1
    

arr = [2, 3, 4, 10, 40]
target = 3

res = search(arr, target)

if res != - 1:
    print(f"Jump Search: Element found at index {res}")
else:
    print("Target not found")