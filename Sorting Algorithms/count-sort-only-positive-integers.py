def count_sort(arr):
    highest=max(arr)
    lowest=min(arr)
    result=[]
    counts=[0 for i in range(lowest, highest+1)]

    for i in arr:
        counts[i]+=1
    
    for i in range(len(counts)):
        if counts[i]!=0:
            result+=counts[i]*[i]
        else:
            continue

    return result
