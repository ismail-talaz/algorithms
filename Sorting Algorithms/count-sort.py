def count_sort(arr):
    highest=max(arr)
    lowest=min(arr)
    result=[0]*len(arr)
    counts=[0 for i in range(lowest, highest+1)]

    for i in arr:
        counts[i-lowest]+=1
    
    for j in range(1, len(counts)):
      counts[j] += counts[j-1]

    for k in reversed(arr):
        result[counts[k-lowest] - 1] = k 
        counts[k-lowest] -= 1

    return result


if __name__ == '__main__':
    arr = [0,0,-2,-90,31,50,50,3,7,77,7,26,5,9]
    count_sort(arr)
    print("Sorted Array:",arr)
