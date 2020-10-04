def merge_sort(array, start, mid, end):
    i, j, k = start, mid + 1, start
    array_c=[0]*(end-start+1)
    for item in range(end-start+1):
        array_c[item]=array[start+item]

    while i <= mid and j <= end:
        if array_c[i-start] < array_c[j-start]:
            array[k] = array_c[i-start]
            i += 1
        else:
            array[k] = array_c[j-start]
            j += 1
        k += 1

    if j>end:
        while i <= mid:
            array[k] = array_c[i-start]
            i += 1
            k += 1
    elif i>mid:
        while j <= end:
            array[k] = array_c[j-start]
            j += 1
            k += 1
 

def merge(array, start, end):
    if start < end:
        mid = (end + start) // 2
        merge(array, start, mid)
        merge(array, mid + 1, end)
        merge_sort(array, start, mid, end)
    


def main():
    size = int(input("enter size"))
    array = list(map(int, input("enter array element separated by space").split()))
    merge(array, 0, size-1)
    print(*array)

if __name__ == "__main__":
    main()
