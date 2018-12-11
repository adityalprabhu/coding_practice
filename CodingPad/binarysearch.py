# Binary Search implementation
# Works only on a sorted array


def binary_search(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = int((low + high)/2)
        print(arr[mid])
        if arr[mid] > x:
            high = mid - 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            return mid

    return -1


if __name__ == '__main__':
    elements = [0, 1, 2, 3, 5, 6, 8, 25, 64]
    print(binary_search(elements, 6))