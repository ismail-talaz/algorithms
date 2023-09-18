def countSortbyDigit(arr,d):

    size=len(arr)
    result=[0]*size
    counts=[0]*10

    for i in range(0, size):
        index=digit(arr[i],d)
        counts[index]+=1
    
    for i in range(1,len(counts)):
        counts[i] += counts[i - 1]
    
    for i in range(size-1,-1,-1):
        index=digit(arr[i],d)
        result[counts[index]-1]=arr[i]
        counts[index]-=1

    for i in range(0, size):
        arr[i] = result[i]

def digit(num,d):
    num=str(num)
    if len(num)>=d:
        return int(num[-d])
    else:
        return 0
    
def radixSort(arr):
    maximum=max(arr)
    d=0
    while maximum != 0:
        maximum //= 10
        d += 1
    
    for i in range(1,d+1):
        countSortbyDigit(arr,i)

if __name__ == '__main__':
    data = [232,445,63,1,1,34,99,53,56,43,77,124]
    radixSort(data)
    print(data)

