# Quicksort implementation

# function that swaps the elements
def swap(arr, left, right):
    tmp = arr[left]
    arr[left] = arr[right]
    arr[right] = tmp

# function that partitions the elements
# and arranges the left array where elements < pivot and right > pivot
def partition(arr, left, right):

    # pivot selection can also be in some other way
    # random?
    pivot = arr[int((left+right)/2)]

    while left <= right:
        while arr[left] < pivot:
            left += 1

        while arr[right] > pivot:
            right -= 1

        if left <= right:
            swap(arr, left, right)
            left += 1
            right -= 1

    return left

# gets a partition and sorts the array for each partition
def quicksort(arr, left, right):
    index = partition(arr, left, right)

    if left < index-1:
        quicksort(arr, left, index-1)

    if index < right:
        quicksort(arr, index, right)

    return arr

# initial qsort
def quicksort_initial(arr):
    return quicksort(arr, 0, len(arr)-1)


if __name__ == '__main__':
    elements = [3,2,5,25,8,0,1,64,6]
    print(quicksort_initial(elements))

