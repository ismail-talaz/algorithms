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

    def minHeapify(self,i):
        left=self.leftChild(i)
        right=self.rightChild(i)
        smallest=i

        if left<self.heapSize and self.arr[left]<self.arr[i]:
            smallest=left
        if right<self.heapSize and self.arr[right]<self.arr[smallest]:
            smallest=right

        if i!=smallest:
            self.arr[smallest],self.arr[i]=self.arr[i],self.arr[smallest]
            self.minHeapify(smallest)
    
    def removeRoot(self): 

        if self.heapSize <= 0:
            return None
        if self.heapSize == 1:             # The running time of removeRoot is O(logn)
            self.heapSize -= 1
            return self.arr[0]
        
        min=self.arr[0]
        self.arr[0]=self.arr[self.heapSize-1]
        self.heapSize-=1

        self.minHeapify(0)

        return min

    def insertKey(self,key):

        self.heapSize+=1
        i=self.heapSize-1
        self.arr[i]=key

        while i!=0 and self.arr[i]<self.arr[self.parent(i)]:
            self.arr[i],self.arr[self.parent(i)]=self.arr[self.parent(i)],self.arr[i]
            i=self.parent(i)

    def decreaseKey(self,i,key):
        if self.arr[i]<key:return
        while i>0 and self.arr[self.parent(i)]>key:       # Running time O(logn)
            self.arr[i]=self.arr[self.parent(i)]
            i=self.parent(i)
        self.arr[i]=key
        
    def removeKey(self,i):
        if self.arr[i]<self.arr[self.heapSize-1]:
            self.arr[i]=self.arr[self.heapSize-1]
            self.minHeapify(i)                            # Running time O(logn)
        else:
            self.decreaseKey(i,self.arr[self.heapSize-1])
        self.heapSize-=1

    def buildHeap(self,load):

        for key in load:                # Time Complexity O(nlgn)
            self.insertKey(key)

    def buildHeap2(self,load): 
        self.arr=load
        self.heapSize=len(load)
        last=(len(self.arr)//2)-1                   # Time Complexity O(N) 
        for i in range(last,-1,-1):
            self.minHeapify(i)

if __name__ == '__main__':

    myArray=[1,2,3,4,5,6,7]
    myHeap=Heap(len(myArray))
    myHeap.buildHeap(myArray)
    myHeap.decreaseKey(4,1)
    myHeap.print()