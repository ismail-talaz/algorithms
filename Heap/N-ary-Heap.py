class Heap:

    def __init__(self,maxSize,N):

        self.N=N
        self.maxSize=maxSize
        self.heapSize=0
        self.arr=[None]*maxSize

    def parent(self,i):
        return (i-1)//self.N
    
    def children(self,i):
        children=[]
        for j in range(1,self.N+1):
            children.append(self.N*i+j)
        return children

    def maxHeapify(self,i):

        largest=i
        for child in self.children(i):
            if child<self.heapSize and self.arr[child]>self.arr[largest]:
                largest=child
        if i!=largest:
            self.arr[largest],self.arr[i]=self.arr[i],self.arr[largest]
            self.maxHeapify(largest)

    def removeRoot(self):

        if self.heapSize <= 0:
            return None
        if self.heapSize == 1:
            self.heapSize -= 1
            return self.arr[0]
        
        max=self.arr[0]
        self.arr[0]=self.arr[self.heapSize-1]
        self.heapSize-=1

        self.maxHeapify(0)

        return max
    
    def removeKey(self,i):
        if self.arr[i]>self.arr[self.heapSize-1]:
            self.arr[i]=self.arr[self.heapSize-1]
            self.maxHeapify(i)                      
        else:
            self.increaseKey(i,self.arr[self.heapSize-1])
        self.heapSize-=1
    
    def insertKey(self,key):

        self.heapSize+=1
        i=self.heapSize-1
        self.arr.append(key)

        while i!=0 and self.arr[i]>self.arr[self.parent(i)]:
            self.arr[i],self.arr[self.parent(i)]=self.arr[self.parent(i)],self.arr[i]
            i=self.parent(i)
    
    def increaseKey(self,i,key):
        if self.arr[i]>key:return
        while i>0 and self.arr[self.parent(i)]<key:
            self.arr[i]=self.arr[self.parent(i)]
            i=self.parent(i)
        self.arr[i]=key

    def buildHeap(self,load):
        self.arr=load
        self.heapSize=len(load)
        for i in range(((self.heapSize-1)//self.N),-1,-1):
            self.maxHeapify(i)
    
    def print(self):
        print(self.arr[:self.heapSize])

if __name__ == '__main__':

    myArray=[24,1,45,65,7,21,76,55,98]
    myHeap=Heap(len(myArray),3)
    myHeap.buildHeap(myArray)
    myHeap.insertKey(99)
    myHeap.print()
