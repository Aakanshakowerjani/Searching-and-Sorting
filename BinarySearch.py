def BinarySearch(array, start, end, data):
    mid = (start + end) // 2
    if array[mid] == data:
        return mid
    elif array[mid] > data:
        return BinarySearch(array, start, mid - 1, data)
    else:
        return BinarySearch(array, mid + 1, end, data)


def main():
    size = int(input("enter the size of array"))
    array = list(map(int, input("enter the arrays element separated by space").split()))
    element = int(input("enter the element to be seached"))
    array.sort()
    print('sorted array is',*array)
    print("element found at index", BinarySearch(array, 0, size - 1, element) + 1)


if __name__ == "__main__":
    main()
