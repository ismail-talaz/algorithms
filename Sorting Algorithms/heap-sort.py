class Heap:

    def __init__(self,maxSize):

        self.maxSize=maxSize
        self.heapSize=0
        self.arr=[None]*maxSize
    
    def parent(self,i):
        return (i-1)//2

    def leftChild(self,i):
        return 2*i+1
    
    def rightChild(self,i):
        return 2*i+2

    def print(self):
        print(self.arr[:self.heapSize])

    def maxHeapify(self,i):
        left=self.leftChild(i)
        right=self.rightChild(i)
        largest=i

        if left<self.heapSize and self.arr[left]>self.arr[i]:
            largest=left
        if right<self.heapSize and self.arr[right]>self.arr[largest]:
            largest=right

        if i!=largest:
            self.arr[largest],self.arr[i]=self.arr[i],self.arr[largest]
            self.maxHeapify(largest)
    
    def removeRoot(self): 

        if self.heapSize <= 0:
            return None
        if self.heapSize == 1:             # The running time of removeRoot is O(logn)
            self.heapSize -= 1
            return self.arr[0]
        
        max=self.arr[0]
        self.arr[0]=self.arr[self.heapSize-1]
        self.heapSize-=1

        self.maxHeapify(0)

        return max

    def insertKey(self,key):

        self.heapSize+=1
        i=self.heapSize-1
        self.arr.append(key)

        while i!=0 and self.arr[i]>self.arr[self.parent(i)]:
            self.arr[i],self.arr[self.parent(i)]=self.arr[self.parent(i)],self.arr[i]
            i=self.parent(i)

    def increaseKey(self,i,key):
        if self.arr[i]>key:return
        while i>0 and self.arr[self.parent(i)]<key:       # Running time O(logn)
            self.arr[i]=self.arr[self.parent(i)]
            i=self.parent(i)
        self.arr[i]=key
        
    def removeKey(self,i):
        if self.arr[i]>self.arr[self.heapSize-1]:
            self.arr[i]=self.arr[self.heapSize-1]
            self.maxHeapify(i)                            # Running time O(logn)
        else:
            self.increaseKey(i,self.arr[self.heapSize-1])
        self.heapSize-=1

    def buildHeap(self,load):

        for key in load:                # Time Complexity O(nlgn)
            self.insertKey(key)

    def buildHeap2(self,load): 
        self.arr=load
        self.heapSize=len(load)
        last=(len(self.arr)//2)-1                   # Time Complexity O(N) 
        for i in range(last,-1,-1):
            self.maxHeapify(i)
    
    def heapSort(self):
        
        for i in range(self.heapSize):
            largest=self.removeRoot()
            self.arr[self.maxSize-i-1]=largest
        print(self.arr)

if __name__ == '__main__':

    myArray=[200,2,44,53,99,23,49]
    myHeap=Heap(len(myArray))
    myHeap.buildHeap2(myArray)
    myHeap.heapSort()
    

    

    




