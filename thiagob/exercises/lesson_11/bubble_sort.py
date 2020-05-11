def bubble_sort(arr):
    while(True):
        swapped = False

        for i in range(1, len(arr)):
            if arr[i] < arr[i-1]:
                smaller = arr[i]
                arr[i] = arr[i-1]
                arr[i-1] = smaller

                swapped = True

        if not swapped:
            break

    return arr

def bubble_sort_improved(arr):
    limit = len(arr)
    while(True):
        swapped = False

        for i in range(1, limit):
            if arr[i] < arr[i-1]:
                arr[i], arr[i-1] = arr[i-1], arr[i]
                swapped = True

        if not swapped:
            break

        limit = limit - 1

    return arr



ints = [4, 6, 0, 9, 5]
print(bubble_sort(ints))

ints = [4, 6, 0, 9, 5]
print(bubble_sort_improved(ints))