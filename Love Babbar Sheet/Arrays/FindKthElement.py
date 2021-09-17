# Approach 1: O(nlogn) - Using Sort


def kthSmallest(arr, n, k):

    # Sort the array

    arr.sort()


# return kth element in the sorted array
    return arr[k-1]

# driver code


if __name__ == '__main__':
    arr = [12, 67, 45, 99, 102]
    n = len(arr)
    k = 2
    print('Kth smallest element is: ', kthSmallest(arr, n, k))

# Approach 2: Quick Select

    # This is an optimization over method 1 if QuickSort is used as a sorting algorithm in first step.
    # In QuickSort, we pick a pivot element, then move the pivot element to its correct position
    # and partition the surrounding array.
    # The idea is, not to do complete quicksort, but stop at the point where pivot itself is k’th smallest element.
    # Also, not to recur for both left and right sides of pivot, but recur for one of them according to the position of pivot.
    # The worst case time complexity of this method is O(n2), but it works in O(n) on average.
