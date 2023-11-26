class Stack:

    def __init__(self):
        self.arr=[]
    
    def push(self,item):
        self.arr.append(item)
    
    def pop(self):
        if self.isEmpty():return False
        return self.arr.pop()

    def isEmpty(self):
        return self.arr==[]
    
    def peek(self):
        return self.arr[-1]

    def print(self):
        print(self.arr)
