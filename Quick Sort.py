def partition(array, lower_bound, upper_bound):
    start = lower_bound
    end = upper_bound
    pivot = lower_bound
    while start < end:
        while array[pivot] >= array[start] and start<upper_bound:
            start += 1
        while array[pivot] < array[end] and end>lower_bound:
            end -= 1
        if start < end:
            array[start], array[end] = array[end], array[start]
    array[end], array[pivot] = array[pivot], array[end]
    return end


def quicksort(array, lower_bound, upper_bound):
    if lower_bound<upper_bound:
        element = partition(array, lower_bound, upper_bound)
        quicksort(array, lower_bound, element - 1)
        quicksort(array, element + 1, upper_bound)


def main():
    size = int(input("enter size of array"))
    array = list(map(int, input("enter element of array separated by space").split()))
    quicksort(array, 0, size-1)
    print(*array)


if __name__ == "__main__":
    main()
