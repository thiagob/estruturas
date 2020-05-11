import merge_sort

def simple_search(arr, element):
    for i in range(len(arr)):
        if arr[i] == element:
            return i
    
    return None


def binary_search(arr, element, left, right):
    mid = int((right + left) / 2)
    if arr[mid] == element:
        return mid
    elif (left > right or element > arr[right] or element < arr[left]):
        return None
    elif element < arr[mid]:
        return binary_search(arr, element, left, mid -1)
    else:
        return binary_search(arr, element, mid + 1, right)


ints = [4, 6, 0, 9, 5]
print(simple_search(ints, 4))

merge_sort.merge_sort(ints)

print(binary_search(ints, 4, 0, len(ints)-1))
print(binary_search(ints, 7, 0, len(ints)-1))
