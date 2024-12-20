####################### Stacks using Linked List #######################


class Node():
    def __init__(self, node_value):
        self.value = node_value
        self.next_node_reference = None
        # self.prev_node_reference = None


class Stack_LinledList():
    def __init__(self):
        self.head = None
        self.tail = None
        
        
    def __iter__(self):
        iter_node = self.head
        while iter_node:
            yield iter_node
            iter_node = iter_node.next_node_reference
        
    def create_Stack_LinledList(self, node_value):
        New_node = Node(node_value)
        self.head = New_node
        self.tail = New_node
        
        
    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False
        
    def push(self,node_value):
        New_node = Node(node_value)
        New_node.next_node_reference = self.head 
        self.head = New_node
        
    def pop(self):
        if self.isEmpty() == True:
            print("There is nothing in the Stack")
            return
        else:
            poped = self.head.value
            self.head  = self.head.next_node_reference
            return poped
        
        
        
    def peek(self):
        if self.isEmpty() == True:
            print("There is nothing in the Stack")
            return
        else:
            peeked = self.head.value
            return peeked



    def delete(self):
        self.head = None
        self.tail = None




My_SLL = Stack_LinledList()
My_SLL.create_Stack_LinledList(1)

print([node.value for node in My_SLL ])

My_SLL.isEmpty()
My_SLL.push(2)
My_SLL.push(3)
My_SLL.push(4)
My_SLL.push(5)


print([node.value for node in My_SLL ])

print(My_SLL.pop())

print([node.value for node in My_SLL ])


print(My_SLL.peek())

print([node.value for node in My_SLL ])



My_SLL.delete()

print([node.value for node in My_SLL ])



























































