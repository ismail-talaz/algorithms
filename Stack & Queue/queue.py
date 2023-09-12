class Queue:

    def __init__(self):
        self.arr=[]

    def enQueue(self,item):
        self.arr.append(item)
    
    def deQueue(self):
        if self.isEmpty():return False
        return self.arr.remove(0)
    
    def isEmpty(self):
        return self.arr==[]
    
    def front(self):
        return self.arr[0]
    
    def print(self):
        print(self.arr)
