####################### Queue using Linked List #######################

######### Video 6: 
    
    
class Node():
    def __init__(self, value):
        self.value = value
        self.next_node_reference = None
    

class LinkedList():
    def __init__(self):
        self.head = None 
        self.tail = None
        
    def __iter__(self):
        iter_node = self.head
        while iter_node != self.tail:
            yield iter_node
            iter_node = iter_node.next_node_reference
        yield self.tail
            

    def create_LL(self,node_vlue):
        New_node = Node(node_vlue)
        # self.head.next_node_reference = New_node
        self.head = New_node
        # self.tail.next_node_reference = New_node
        self.tail = New_node
        # New_node.next_node_reference = New_node


# Inserting at the end (tail)
    def insert_node(self,node_vlue):
        New_node = Node(node_vlue)
        New_node.next_node_reference = self.head
        self.tail.next_node_reference = New_node
        self.tail = New_node
    
# Removing from the beginning
    def remove_node(self):
        poped = self.head.value
        self.head = self.head.next_node_reference 
        self.tail.next_node_reference =self.head
        return poped 
        
        
    
class Queue():
    def __init__(self):
        self.Queue = LinkedList()
        self.top = self.Queue.tail
        self.start = self.Queue.head
        
        
        
    def __str__(self):
        Values =[str(x.value) for x in self.Queue]
        print("\n>>> Returning the queue >>> \n")
        return "<-".join(Values) + '\n'
    
    def create_queue(self, value):
        self.Queue.create_LL(value)
        self.top = self.Queue.tail
        self.start = self.Queue.head
        
        
        
    
    def isEmpty(self):
        if self.top == None:
            return True
        else:
            return False
    
    
    def enqueue(self, value):
        # New_node = Node(value)
        # New_node.next_node_reference = self.start
        # self.top.next_node_reference = New_node
        # self.top = New_node
        self.Queue.insert_node(value)
        self.top = self.Queue.tail
        self.start = self.Queue.head
        
        
        
    def dequeue(self):
        if self.top == self.start:
            print("self.top == self.start")
        dequeued = self.Queue.remove_node()
        self.top = self.Queue.tail
        self.start = self.Queue.head

        return dequeued
        
    
    def peek(self):
        peeked = self.start.value
        return peeked
    
    
    def delete(self):
        self.Queue = None
        self.top = None
        self.start = None
        print("Deleted")
        return
        
        
        
        
        
        
My_Queue = Queue()
        
print(My_Queue.isEmpty())    
      

My_Queue.create_queue(0)
My_Queue.enqueue(1) 
My_Queue.enqueue(2) 
My_Queue.enqueue(3) 
My_Queue.enqueue(4) 

print(My_Queue)

print("My_Queue.dequeue()  == >",My_Queue.dequeue())

print(My_Queue)

print("---------")    
My_Queue.enqueue(5)    
print(My_Queue)
print("My_Queue.dequeue()  == >",My_Queue.dequeue()) 
print("My_Queue.dequeue()  == >",My_Queue.dequeue()) 
print("My_Queue.dequeue()  == >",My_Queue.dequeue()) 
print("My_Queue.dequeue()  == >",My_Queue.dequeue())
print("---------") 
print("My_Queue.dequeue()  == >",My_Queue.dequeue()) 
print("My_Queue.dequeue()  == >",My_Queue.dequeue()) 
print("My_Queue.peek()  == >",My_Queue.peek()) 

print(My_Queue.isEmpty()) 

print(My_Queue)     
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        