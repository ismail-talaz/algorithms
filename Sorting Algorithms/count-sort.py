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
