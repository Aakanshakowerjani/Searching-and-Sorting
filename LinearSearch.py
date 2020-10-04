def LinearSearch(array, size, element):
    for item in range(size):
        if array[item] == element:
            return item
    return


def main():
    size = int(input("enter size of array"))
    array = list(map(int, input("enter elements of array").split()))
    element = int(input("enter element to be search"))
    found = LinearSearch(array, size, element)
    if found == None:
        print("element not found")
    else:
        print("element found at index", found + 1)


if __name__ == "__main__":
    main()
