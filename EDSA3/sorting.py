def bubble_sort(items):
    """ the bubble sort algorithm takes in an unsorted list of numbers or strings.
    returns a list in ascending order.

    Parameters
    ----------
    items : list
        list of unordered numbers words or strings
        Returns
        -------
        list
            list of elements in items in ascending order """
    out = items.copy() # in place protection on items
    for i in range(len(out)):
        for j in range(len(out)-1-i):
            if out[j] > out[j+1]:
                out[j], out[j+1] = out[j+1], out[j]     # Swap!

    return out

def merge(left, right):
    """Merge sort merging function."""

    left_index, right_index = 0, 0
    result = []
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result += left[left_index:]
    result += right[right_index:]
    return result


def merge_sort(array):
    """ the merge sort algorithm takes in an unsorted list of numbers or strings.
    returns a list in ascending order.

    Parameters
    ----------
    array :
        list of unordered numbers words or strings

    Returns
    -------
    list
    list of elements in items in ascending order """

    if len(array) <= 1:  # base case
        return array

    # divide array in half and merge sort recursively
    half = len(array) // 2
    left = merge_sort(array[:half])
    right = merge_sort(array[half:])

    return merge(left, right)

def quick_sort(items, index=-1):
    """
    the quick sort algorithm takes in an unsorted list of numbers or strings.
    returns a list in ascending order.

    Parameters
    ----------
    items : list
        list of unordered numbers words or strings
    index: int, optional
        index number at which to choose the split value
        default set to the last item in the input list

    Returns
    -------
    list
        list of elements in items in ascending order
    """
    len_i = len(items)

    if len_i <= 1:

        return items

    pivot = items[index]
    small = []
    large = []
    dup = []
    for i in items:
        if i < pivot:
            small.append(i)
        elif i > pivot:
            large.append(i)
        elif i == pivot:
            dup.append(i)

    small = quick_sort(small)
    large = quick_sort(large)

    return small + dup + large
