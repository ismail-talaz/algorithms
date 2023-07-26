def selection_sort(arr):
    for a in range(len(arr)):
        min_idx=a
        for b in range(a+1,len(arr)):
            if arr[b]<arr[min_idx]:
                min_idx=b
        if arr[min_idx]<arr[a]:
            arr[min_idx],arr[a]=arr[a],arr[min_idx]
    return arr


if __name__ == '__main__':
    arr = [1,1,0,31,50,3,3,3,3,3,7,-1,26,26,555,9]
    selection_sort(arr)
    print("Sorted Array:",arr)
