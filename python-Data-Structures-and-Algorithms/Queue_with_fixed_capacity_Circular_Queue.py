####################### Queue using Python List with fixed capacity (Circular Queue) #######################


######### Video 4: Circular Queue (with fixed capacity)

# import numpy as np

class Circular_Queue():
    def __init__(self,max_size):
        self.max_size = max_size
        # self.queue = [ None for i in range(self.max_size)]
        self.queue = [ None ] * self.max_size
        self.top = -1
        self.start = -1 
        
        
    def __str__(self):
        values = [str(x) for x in self.queue]
        return " <- ".join(values)
        
    def isEmpty(self):
        # bools = [x==None for x in self.queue]
        # if False not in bools:
        #     return True
        # else:
        #     return False
        if self.top == -1:
            return True
        else:
            return False
        
        
    def isFull(self):
        # if None not in self.queue:
        if self.top +1 == self.start:
            return True
        elif self.start == 0 and self.top +1 == self.max_size:
            return True 
        else:
            return False
        
    
    def enqueue(self, value):
        if self.isFull():
            print("The queue is full")
            return 
        else:
            if self.isEmpty():
                self.start += 1
                
            self.top += 1
            
            # if self.top == 0:
            #     pass
            # else:
            # print('self.top before', self.top)
            self.top = self.top % self.max_size 
            # print('self.top after', self.top)
            self.queue[self.top] = value


    def dequeue(self):
        if self.isEmpty():
            print("The queue is empty")
            return
        else:
            dequeued = self.queue[self.start]
            self.queue[self.start] = None
            self.start += 1
            self.start = self.start % self.max_size 
        return dequeued
        


    def peek(self):
        if self.isEmpty():
            print("The queue is empty")
            return
        else:
            peeked = self.queue[self.start]
        return peeked


    def delete(self):     
        # self.queue = [ None for i in range(self.max_size)]
        self.queue = [ None ] * self.max_size
        self.top = -1
        self.start = -1 
        return "Deleted"






My_Circular_Queue = Circular_Queue(3)

print(My_Circular_Queue.isEmpty())

print("-------")

My_Circular_Queue.enqueue(1)
print('My_Circular_Queue.top',My_Circular_Queue.top)
My_Circular_Queue.enqueue(2)
print('My_Circular_Queue.top',My_Circular_Queue.top)
My_Circular_Queue.enqueue(3)
print('My_Circular_Queue.top',My_Circular_Queue.top)
My_Circular_Queue.enqueue(4)
# print('My_Circular_Queue.top',My_Circular_Queue.top)
# My_Circular_Queue.enqueue(5)
# print('My_Circular_Queue.top',My_Circular_Queue.top)

# My_Circular_Queue.enqueue(6)

print("-------")
print(My_Circular_Queue)

print("-------")

print("My_Circular_Queue.dequeue() == ",My_Circular_Queue.dequeue())
print("My_Circular_Queue.dequeue() == ",My_Circular_Queue.dequeue())

print(My_Circular_Queue)
My_Circular_Queue.enqueue(4)
print(My_Circular_Queue)
My_Circular_Queue.enqueue(5)
print(My_Circular_Queue)
print("My_Circular_Queue.dequeue() == ",My_Circular_Queue.dequeue())
print(My_Circular_Queue)
My_Circular_Queue.enqueue(6)
print("My_Circular_Queue.dequeue() == ",My_Circular_Queue.dequeue())
print(My_Circular_Queue)
# print("-------")


print("-------")
print("My_Circular_Queue.peek() == ",My_Circular_Queue.peek())
print("-------")
print("My_Circular_Queue.delete() == ",My_Circular_Queue.delete())
print(My_Circular_Queue)








