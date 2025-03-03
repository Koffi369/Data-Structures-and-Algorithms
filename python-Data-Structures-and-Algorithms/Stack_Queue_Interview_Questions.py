####################### Queue & Stack Interview Questions #######################
        
########### Video 1     
'''
Question 1: Use a single python list to implement 3 stacks
'''

# class stack:
#     def __init__(self, max_size):
#         self.max_size =  max_size
#         self.list = [None] * self.max_size
#         self.total_num_stack = 3
        
#         self.st_pt1 = 0
#         self.st_pt2 = 1
#         self.st_pt3 = 2
        
#         self.ct_st_pt1 = 0
#         self.ct_st_pt2 = 0
#         self.ct_st_pt3 = 0
        
        
#     def __str__(self):
#         values = [str(x) for x in self.list]
#         return " - ".join(values)
        
        
        
#     def isFull(self, stack_id): #stack_num is the id of the stack
#         if stack_id == 1:
#             if self.ct_st_pt1 == int(self.max_size/3):
#                 return True
#             else:
#                 return False
            
            
#         if stack_id == 2:
#             if self.ct_st_pt2 == int(self.max_size/3):
#                 return True
#             else:
#                 return False
            
#         if stack_id == 3:
#             if self.ct_st_pt3 == int(self.max_size/3):
#                 return True
#             else:
#                 return False
            
            
            
#     def isEmpty(self, stack_id):
#         if stack_id == 1 and self.ct_st_pt1 == 0:
#             return True
#         else:
#             return False
        
        
#         if stack_id == 2 and self.ct_st_pt2 == 0:
#             return True
#         else:
#             return False
            

#         if stack_id == 3 and self.ct_st_pt3 == 0:
#             return True
#         else:
#             return False  
        
        
        

        
#     def add_elmt(self, value, stack_id):
        
#         if stack_id == 1:
#             if self.isFull(stack_id):
#                 return f"the stack {stack_id} is full"
            
#             self.list[self.st_pt1] =  value
#             self.ct_st_pt1 += 1
            
#             if self.st_pt1 + 3 > self.max_size -1 :
#                 return
#             self.st_pt1 +=3
            

                  
#         if stack_id == 2:
#             if self.isFull(stack_id):
#                 return f"the stack {stack_id} is full"
#             self.list[self.st_pt2] =  value
            
#             self.ct_st_pt2 += 1
#             if self.st_pt2 + 3 > self.max_size -1 :
#                 return
#             self.st_pt2 +=3
            
#         if stack_id == 3:
#             if self.isFull(stack_id):
#                 return f"the stack {stack_id} is full"
#             self.list[self.st_pt3] =  value    
            
#             self.ct_st_pt3 += 1
#             if self.st_pt3 + 3 > self.max_size -1 :
#                 return
            
#             self.st_pt3 +=3
        
        

    
#     def remove_elmt(self, stack_id):
        
#         if stack_id == 1:
#             if self.isEmpty(stack_id):
#                 return f"the stack {stack_id} is Empty"
#             # print(self.st_pt1)
#             poped = self.list[self.st_pt1]
#             self.list[self.st_pt1] = None
#             self.st_pt1 -=3
#             self.ct_st_pt1 -= 1
#             return poped
        
        
#         if stack_id == 2:
#             if self.isEmpty(stack_id):
#                 return f"the stack {stack_id} is Empty"
#             poped = self.list[self.st_pt2]
#             self.list[self.st_pt2] = None
#             self.st_pt2 -=3
#             self.ct_st_pt2 -= 1
#             return poped
        
        
#         if stack_id == 3:
#             if self.isEmpty(stack_id):
#                 return f"the stack {stack_id} is Empty"
#             poped = self.list[self.st_pt3]
#             self.list[self.st_pt3] = None
#             self.st_pt3 -=3
#             self.ct_st_pt3 -= 1
#             return poped
        
  
        
# My_Stack = stack(9)

    
# # add_elmt(self, value, stack_id)    
        
# My_Stack.add_elmt(1,1)
# My_Stack.add_elmt(2,1)
# My_Stack.add_elmt(3,1)
        
        
        
# print(My_Stack)     
        
        
# print(My_Stack.add_elmt(4,1))    
        
# print(My_Stack)         
        
# print(" ----------------------- ")   
        
# # remove_elmt(self, stack_id)      
        
# print( "My_Stack.remove_elmt(1) == >",My_Stack.remove_elmt(1)   ) 
# print( "My_Stack.remove_elmt(1) == >",My_Stack.remove_elmt(1)   ) 
# print( "My_Stack.remove_elmt(1) == >",My_Stack.remove_elmt(1)   ) 
# print( "My_Stack.remove_elmt(1) == >",My_Stack.remove_elmt(1)   ) 
        
        
        
########### Video 2     
'''
Question 2: How would you design a stack which, in addition to push and pop has
a function/method min which returns the minimum elmt of the stack
NB: Push, Pop, and Min should all operate in O(1)
'''    


class Node:
    def __init__(self, value,minimum):
        self.value = value
        self.minimum = minimum
        self.next_node_reference = None



class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
        
    def __iter__(self):
        iter_node = self.head
        while iter_node:
            yield iter_node
            iter_node = iter_node.next_node_reference
            
            
class stack:
    def __init__(self):
        self.stack = LinkedList()
        self.min = 1000000
        
        
    def __str__(self):
        values = [str((x.value,x.minimum)) for x in self.stack]
        return " <- ".join(values)
        
        
    def isEmpty(self):
        if self.stack.head == None:
            return True
        return False
        
        
    def push(self, value):
        
        if value < self.min:
            self.min = value
            
        New_node = Node(value, self.min)
        
        New_node.next_node_reference = self.stack.head
        self.stack.head = New_node
        
        
    def pop(self):
        if self.isEmpty():
            print("The Stack is empty")
            return
        poped = self.stack.head.value
        if self.stack.head.next_node_reference:
            self.stack.head = self.stack.head.next_node_reference
        else:
            self.stack.head = None

        return poped
        
        

    def mini(self):
        if self.isEmpty():
            print("The Stack is empty")
            return
        minimum = self.stack.head.minimum
        return minimum






My_Stack = stack()

    


My_Stack.push(2)
My_Stack.push(3)
My_Stack.push(1)

print(My_Stack)

print( " My_Stack.mini()",My_Stack.mini())

print( " My_Stack.pop()",My_Stack.pop())
print(My_Stack)
print( " My_Stack.mini()",My_Stack.mini())

print(My_Stack)




















        
        
        