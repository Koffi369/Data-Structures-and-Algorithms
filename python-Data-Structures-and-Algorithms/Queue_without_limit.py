####################### Queue using Python List without size limit #######################


######### Video 3: Queue implementation using Python List without size limit



class Queue():
    def __init__(self):
        self.queue = []
        
    def __str__(self):
        values = [str(x) for x in self.queue]
        return "->".join(values)
        
    def isEmpty(self):
        if self.queue == []:
            # print("The queue is empty")
            return True
        else:
            return False
        
    def enqueue(self, value):
        self.queue = [value] + self.queue  
        
    def dequeue(self):
        if self.isEmpty():
            print("The Queue is empty")
            return
        else:
            dequeued = self.queue[-1]
            self.queue = self.queue[:-1]
            return dequeued
        
    def peek(self):
        if self.isEmpty():
            print("The Queue is empty")
            return
        else:
            peeked = self.queue[-1]
            return peeked
    def delete(self):
        self.queue = None
        
        
    
My_queue = Queue()

# print(My_queue.isEmpty())

My_queue.enqueue(1)
My_queue.enqueue(2)
My_queue.enqueue(3)
My_queue.enqueue(4)

print(My_queue)

print("=========")
print("My_queue.peek() ==>", My_queue.peek())
print("=========")
print('My_queue.dequeue() ==>',My_queue.dequeue())
print("My_queue.peek() ==>", My_queue.peek())
print("=========")
print(My_queue)











