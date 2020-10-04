def insertionSort(array, size):
    for element in range(1, size):
        current = array[element]
        previous = element - 1
        while previous >= 0 and array[previous] > current:
            array[previous + 1] = array[previous]
            previous -= 1
        array[previous + 1] = current

    return array


def main():
    size = int(input("enter size of array"))
    array = list(map(int, input("enter element of array separated by space").split()))
    print(insertionSort(array, size))


if __name__ == "__main__":
    main()
