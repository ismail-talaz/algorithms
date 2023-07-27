def bubble_sort(arr):
    swapped=True
    while swapped:
        swapped=False
        for a in range(len(arr)-1):
            if arr[a]>arr[a+1]:
                arr[a],arr[a+1]=arr[a+1],arr[a]
                swapped=True


if __name__ == '__main__':
    arr = [30,25,32,165,23,5,92]
    bubble_sort(arr)
    print("Sorted Array:",arr)
