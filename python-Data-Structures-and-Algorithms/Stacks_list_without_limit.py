####################### Stacks Using Python List Without Size limit #######################


######### Video 3: Create a Stack using Python List without size limit


class stack():
    def __init__(self):
        self.list = []

    def __str__(self):
        # values = self.list.reverse()
        # print(values)
        # print(self.list)
        values = [str(x) for x in self.list] 
        # print(values)
        return '\n'.join(values)  
    
######### Video 4: Operations on Stack using Python List without size limit
    
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
        
    def push(self, elmt):
        # self.list.append(elmt)
        self.list = [elmt] + self.list
        
    def pop(self):
        if self.isEmpty():
            return "There is nothing in the Stack"
        else:
            # print('self.list ======',self.list)
            poped = self.list[0]
            # print("self.list[1:] ====== ", self.list[1:])
            self.list = self.list[1:]
            return poped
        # if self.isEmpty():
        #     return "There is nothing in the Stack"
        # else:
        #     return self.list.pop()
        
    def peek(self):
        if self.isEmpty():
            return "There is nothing in the Stack"
        else:
            peeked = self.list[0]
            return peeked
        
    def delete(self):
        self.list = None  
        









######### Video 4: Operations on Stack 

My_stack = stack()

My_stack.push(1)
My_stack.push(2)
My_stack.push(3)
# print(My_stack.isEmpty())
print(My_stack)
print("##########")
print("Poped: ",My_stack.pop())
print("##########")  
print(My_stack)
print("##########")  
print('Peeked: ', My_stack.peek())
print("##########")  
print(My_stack)






















