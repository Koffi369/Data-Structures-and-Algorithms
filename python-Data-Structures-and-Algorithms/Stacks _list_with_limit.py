####################### Stacks Using Python List With Size limit #######################

######### Video 5: Operations on Stack using Python List with size limit

class Stack():
    def __init__(self, maxSize):
        self.list = []
        self.maxSize = maxSize

    def __str__(self):
        values = [str(x) for x in self.list]
        return "\n".join(values)
     
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
    
    def isFull(self):
        if len(self.list) == self.maxSize:
            return True
        else:
            return False
        
    def push(self, elmt):
        if self.isFull():
            print("The Stack is full")
            return 
        else:
            self.list = [elmt] + self.list
        
    def pop(self):
        if self.isEmpty():
            print("The Stack is Empty")
            return 
        else:  
            poped = self.list[0]
            self.list = self.list[1:]
            return poped
        
    
    def peek(self):
        if self.isEmpty():
            print("The Stack is Empty")
            return 
        else:  
            peeked = self.list[0]
            return peeked


    def delete(self):
        self.list = None  


My_stack = Stack(3)


My_stack.push(1)
My_stack.push(2)
My_stack.push(3)
print("##########")
My_stack.push(4)
print("##########")
print(My_stack)
print("##########")
print(My_stack.pop())
print("##########")
print(My_stack)
print("##########")
print(My_stack.peek())
print("##########")
print(My_stack)







