# python3

import random


def partition3(A, l, r):
    lt = l  # We initiate lt to be the part that is less than the pivot
    i = l   # We scan the array from left to right
    gt = r  # The part that is greater than the pivot
    pivot = A[l]    # The pivot, chosen to be the first element of the array, that why we'll randomize the first elements position
                    # in the quick_sort function.
    while i <= gt:      # Starting from the first element.
        if A[i] < pivot:
            A[lt], A[i] = A[i], A[lt]
            lt += 1
            i += 1
        elif A[i] > pivot:
            A[i], A[gt] = A[gt], A[i]
            gt -= 1
        else:
            i += 1

    return lt, gt


def randomized_quick_sort(array, left, right):
    if left >= right:
        return
    k = random.randint(left, right)
    array[k], array[left] = array[left], array[k]

    lt, gt = partition3(array, left, right)
    randomized_quick_sort(array, left, lt - 1)
    randomized_quick_sort(array, gt + 1, right)


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)
