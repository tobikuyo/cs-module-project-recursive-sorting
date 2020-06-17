# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    if start <= end:
        midpoint = (start + end) // 2
        mid_item = arr[midpoint]

        if mid_item == target:
            return midpoint
        elif target < mid_item:
            return binary_search(arr, target, start, midpoint - 1)
        else:
            return binary_search(arr, target, midpoint + 1, end)

    return -1

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass
