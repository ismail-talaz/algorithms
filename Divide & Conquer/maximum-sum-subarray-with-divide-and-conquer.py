def maximumSubarray(arr,low,high):
    if low==high:                                  # By Divide and Conquer Algorithm
        return [low,high,arr[low]]                 # Time Complexity Big Theta θ(nlogn)
    else:
        mid=(low+high)//2
        left=maximumSubarray(arr,low,mid)
        right=maximumSubarray(arr,mid+1,high)
        cross=findMaxCrossing(arr,low,mid,high)

        if cross[2]>left[2] and cross[2]>right[2]:
            return cross
        elif right[2]>left[2] and right[2]>cross[2]:
            return right
        else:
            return left

def findMaxCrossing(arr,low,mid,high):
    leftmost=rightmost=mid
    leftsum=float('-inf')
    sum=0
    for i in range(mid,low-1,-1):
        sum+=arr[i]
        if sum>leftsum:
            leftsum=sum
            leftmost=i
    rightsum=float('-inf')
    sum=0
    for i in range(mid,high+1):
        sum+=arr[i]
        if sum>rightsum:
            rightsum=sum
            rightmost=i
    return [leftmost,rightmost,max(leftsum,rightsum,leftsum+rightsum-arr[mid])]


if __name__ == '__main__':

    array=[-1,22,2,-2,-2,-2,-2,3,4,5,-23,-2,-1,-2,3,10,-98,9]
    result=maximumSubarray(array,0,len(array)-1)       # Give which part of array you want
    print(f"Maximum Subarray is {array[result[0]:result[1]+1]} and the sum is {result[2]}.")
