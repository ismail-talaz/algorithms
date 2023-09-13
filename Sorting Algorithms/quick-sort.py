def quickSort(arr,p,r):
    
    if p<r:
        q=partition(arr,p,r)
        quickSort(arr,p,q-1)
        quickSort(arr,q+1,r)                           # Worst-case Running Time -> O(n^2) when partition is unbalanced (n-1, 0)
                                                       # Average-case Running Time -> O(nlogn). Any split of constant proportionality yields O(nlogn).
def partition(arr,p,r):                                # Best-case Running Time -> O(nlogn) when partition is balanced (floor(n/2) floor(n/2)-1)
                                                    
    pivot=arr[r]
    i=p-1
    for j in range(p,r):
        if arr[j]<=pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[r]=arr[r],arr[i+1]
    return i+1

 
if __name__ == '__main__':                # In place sorting
    array=[2,4,345,3,56,3444,99,7,68]    
    quickSort(array,0,len(array)-1)   # In order to sort an entire array, the initial call must be quickSort(arr,0,len(arr)-1).
    print(array)
