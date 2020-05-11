def quick_sort(arr, low, high):
    if low < high:

        # pi is partitioning index, arr[p] is now
        # at right place
        partition_index = partition(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quick_sort(arr, low, partition_index - 1)
        quick_sort(arr, partition_index + 1, high)

    return arr


def partition(arr, low, high):
    i = (low-1)         
    pivot = arr[high]     # pivot

    for j in range(low, high):

        # If current element is smaller than the pivot
        if arr[j] < pivot:

            # increment index of smaller element
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)


ints = [4, 6, 0, 9, 5]
print(quick_sort(ints, 0, len(ints)-1))
