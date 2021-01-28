# Python program for recursive binary search.
# Retrun index of x in arr if present, else -1


def binary_search(arr, l, r, x):
    # check base case
    if r >= l:
        mid = l + (r - l) // 2
        # if the element present at middle itself
        # itself

        if arr[mid] == x:
            return mid
        # If element is smaller than mid,
        # then
        # it can only present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, l, mid - 1, x)

        else:
            return binary_search(arr, mid + 1, r, x)

    else:
        # Element not present in array
        return -1

# Driver code
arr = [2, 3, 56, 95, 12, 64, 25, 97, 100, 64, 60, 70]
x = 60

# function call
result = binary_search(arr, 0, len(arr), x)
if result != -1:
    print("Element is present at index :", result)
else:
    print("The element not present in array")
