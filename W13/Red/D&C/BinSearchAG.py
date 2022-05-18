# BINARY SEARCH
# Given a sorted list and a number, x, return True if x is found, False otherwise.
def binarySearch(A, x):
    """A is a sorted array. 
    It returns True if x is found, False eoc."""
    if A is None:
        return False

    # base case
    if len(A) == 0:
        return False

    # recursive case
    m = len(A) // 2

    if x == A[m]:
        return True

    if x < A[m]:
        return binarySearch(A[0:m], x)

    if x > A[m]:
        return binarySearch(A[m + 1:], x)


# Returns the index of x in array A
def binarySearchIndex(A, x):
    if A is None or len(A) == 0:
        return -1

    return _binarySearchIndex(A, x, 0, len(A) - 1)


def _binarySearchIndex(A, x, start, end):  # Using indexes
    # Protection against empty array
    if A is None or len(A) == 0:
        return -1

    # base case
    if start > end:
        return -1

    # Recursive case
    mid = (start + end) // 2
    if x == A[mid]:
        return mid
    elif x < A[mid]:
        return _binarySearchIndex(A, x, start, mid - 1)
    else:
        return _binarySearchIndex(A, x, mid + 1, end)




A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x = 4  # index=3
print(binarySearchIndex(A, x))
