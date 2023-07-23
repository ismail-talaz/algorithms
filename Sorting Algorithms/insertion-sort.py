def insertion_sort(arr):                   # Best Case Time Complexity O(n)
    for i in range(1, len(arr)):           # Average Case Time Complexity O(n^2)
        key = arr[i]                       # Worst Case Time Complexity O(n^2)     
        j = i-1
        while j >= 0 and key < arr[j] :       # Slides the key element to the left until it reaches its position. 
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key


if __name__ == '__main__':
    arr = [30,25,32,165,23,5,92]
    insertion_sort(arr)
    print("Sorted Array:",arr)
