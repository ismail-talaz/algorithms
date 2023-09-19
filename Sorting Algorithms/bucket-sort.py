from insertionsort import insertion_sort
import math


def bucketSort(arr):   # This version of bucket sort is for floats ranges [0,1).
    buckets=[[] for i in range(10)]

    for num in arr:
        index=int(num*10)
        buckets[index].append(num)
    
    result=[]
    for bucket in buckets:
        insertion_sort(bucket)
        result=result+bucket
    
    return result


def bucketSort2(arr): 
    b=int(math.sqrt(len(arr)))  # b: number of buckets
    rng=(max(arr)-min(arr))/b   # rng: range of buckets

    buckets=[[] for i in range(b+1)]

    for num in arr:
        index=int((num-min(arr))/rng)     # On average, insertion sort which runs on each bucket will be O(b^2) running time. O(b^2) is equal to O(n) due to the first line. 
        buckets[index].append(num)        # Totally, running time will be O(bn). 
    
    result=[]
    for bucket in buckets:
        insertion_sort(bucket)
        result=result+bucket
    
    return result


if __name__=='__main__':
    arr=[0.2,0.99,0.74,0.21,0.34,0.89,0.11,0.34,0.23,0.1]
    arr2=[2,3,34,345,546,56,54,5,46,68,0.01,45,0.33,99,-122,-99]
    result1=bucketSort(arr)
    result2=bucketSort2(arr2)
    print(result1,"\n",result2)
    


    