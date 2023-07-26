def mergeSort(arr):            # Time Complexity O(nlogn)
    if len(arr)>1:
        mid=len(arr)//2                          
        left,right=arr[:mid],arr[mid:]
        mergeSort(left)
        mergeSort(right)

        i=j=k=0
    
        while (i<len(left) and j<len(right)):        # MERGE
            if left[i]<right[j]:
                arr[k]=left[i]
                i+=1
            else:
                arr[k]=right[j]
                j+=1
            k+=1
    
        if i<len(left):arr[k:]=left[i:]        # Remaining parts is loaded directly to basis array.
        if j<len(right):arr[k:]=right[j:]    


if __name__ == '__main__':
    array = [-100,-1,1,1,0,31,50,3,3,3,3,3,7,-1,26,26,555,9]
    mergeSort(array)
    print("Sorted array is: ",array)
        
