def selectionSort(array, size):
    for element in range(size):
        min_ele = element
        for item in range(element + 1, size):
            if array[min_ele] > array[item]:
                min_ele = item
        if min_ele != element:
            array[element], array[min_ele] = array[min_ele], array[element]
    return array


def main():
    size = int(input("enter size of array"))
    array = list(map(int, input("enter element of array separated by space").split()))
    print(selectionSort(array, size))


if __name__ == "__main__":
    main()
