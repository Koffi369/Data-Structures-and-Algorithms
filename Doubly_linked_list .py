#######################  Doubly Linked List  ##########################

class Node:
    def __init__(self, node_value = None):
        self.value = node_value
        self.next_node_reference = None
        self.prev_node_reference = None



class Doubly_Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def __iter__(self):
        node = self.head
        while node:
            yield node
            
            if node == self.tail:
                break
            node = node.next_node_reference
        
    def Create_DLL(self,node_value):
        New_node = Node(node_value)
        self.tail = New_node
        self.head = New_node
        
        
    def insert_node_in_DLL(self, node_value, location ):
        New_node = Node(node_value)
        
        if location == 0:
             New_node.next_node_reference = self.head
             self.head.prev_node_reference =  New_node
             self.head = New_node
             
        elif location == -1:
            self.tail.next_node_reference = New_node
            New_node.prev_node_reference = self.tail
            self.tail = New_node
            
        else:
            idx = 0
            iter_node = self.head #will stop at location - 1
            # print("iter_node.value:", iter_node.value)
            while idx < location - 1:
                iter_node = iter_node.next_node_reference
                idx +=1
            
            New_node.next_node_reference = iter_node.next_node_reference
            New_node.prev_node_reference = iter_node
            iter_node.next_node_reference.prev_node_reference = New_node
            iter_node.next_node_reference = New_node
        
        
    def traverse_DLL(self):
        if self.head == None:
            print("Sorry there is nothing in the DLL")
        else:
            iter_node = self.head
            while iter_node != self.tail:
                print(iter_node.value)
                iter_node = iter_node.next_node_reference 
            print(iter_node.value)
        
        
    def reverse_traverse_DLL(self):
        if self.head == None:
            print("Sorry there is nothing in the DLL")
        else:
            iter_node = self.tail
            # while iter_node != self.head:
            while iter_node:
                print(iter_node.value)
                iter_node = iter_node.prev_node_reference 
            # print(iter_node.value)
            
    def search_node_in_DLL(self, node_value):
        if self.head ==None:
            print("Sorry there is nothing in the DLL")
        else:
            iter_node = self.head
            idx = 0
            while iter_node.value != node_value:
                if iter_node == self.tail:
                    return print("Element not found in the DLL")
                    
                else:
                    iter_node = iter_node.next_node_reference 
                    idx +=1
                
            print(f"Element found at idx {idx}")
                
    def delete_node_in_DLL(self, location):
        if self.head == None:
            print("Sorry there is nothing in the DLL")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head.next_node_reference.prev_node_reference = None
                    self.head = self.head.next_node_reference
            elif location == -1:            
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail.prev_node_reference.next_node_reference = None
                    self.tail = self.tail.prev_node_reference 
            else:
                iter_node = self.head
                idx = 0
                
                while idx < location -1:
                    iter_node  = iter_node.next_node_reference
                    idx += 1
                iter_node.next_node_reference = iter_node.next_node_reference.next_node_reference
                iter_node.next_node_reference.prev_node_reference = iter_node
                

    def delete_entire_DLL(self):
        iter_node = self.head
        while iter_node != self.tail:
            iter_node = iter_node.next_node_reference
            iter_node.prev_node_reference = None
        self.head = None
        self.tail = None
                
            



##### Video 1 Creation of a Doubly LL

# DoublyLL= Doubly_Linked_List()

# DoublyLL.Create_DLL(5)

# print([node.value for node in DoublyLL ])





##### Video 4 Inserting a node in a Doubly LL

# DoublyLL= Doubly_Linked_List()

# DoublyLL.Create_DLL(1)
# DoublyLL.insert_node_in_DLL(0,0)
# DoublyLL.insert_node_in_DLL(2,-1)
# DoublyLL.insert_node_in_DLL(1.5,2)

# print([node.value for node in DoublyLL ])





# ##### Video 5 Traversal of a Doubly LL

# DoublyLL= Doubly_Linked_List()

# DoublyLL.Create_DLL(1)
# DoublyLL.insert_node_in_DLL(0,0)
# DoublyLL.insert_node_in_DLL(2,-1)
# DoublyLL.insert_node_in_DLL(1.5,2)

# # print([node.value for node in DoublyLL ])

# DoublyLL.traverse_DLL()


# ##### Video 6 Reverse traversal of a Doubly LL

# DoublyLL= Doubly_Linked_List()

# DoublyLL.Create_DLL(1)
# DoublyLL.insert_node_in_DLL(0,0)
# DoublyLL.insert_node_in_DLL(2,-1)
# DoublyLL.insert_node_in_DLL(1.5,2)

# print([node.value for node in DoublyLL ])

# DoublyLL.reverse_traverse_DLL()


# ##### Video 7 Searching for an element in a Doubly LL

# DoublyLL= Doubly_Linked_List()

# DoublyLL.Create_DLL(1)
# DoublyLL.insert_node_in_DLL(0,0)
# DoublyLL.insert_node_in_DLL(2,-1)
# DoublyLL.insert_node_in_DLL(1.5,2)

# print([node.value for node in DoublyLL ])

# DoublyLL.search_node_in_DLL(1.5)





# ##### Video 10 Deletion of a node in a Doubly LL

# DoublyLL= Doubly_Linked_List()

# DoublyLL.Create_DLL(1)
# DoublyLL.insert_node_in_DLL(0,0)
# DoublyLL.insert_node_in_DLL(2,-1)
# DoublyLL.insert_node_in_DLL(1.5,2)

# print([node.value for node in DoublyLL ])

# DoublyLL.delete_node_in_DLL(-1)

# print([node.value for node in DoublyLL ])



##### Video 11 Deletion of the entire Doubly LL

DoublyLL= Doubly_Linked_List()

DoublyLL.Create_DLL(1)
DoublyLL.insert_node_in_DLL(0,0)
DoublyLL.insert_node_in_DLL(2,-1)
DoublyLL.insert_node_in_DLL(1.5,2)

print([node.value for node in DoublyLL ])

DoublyLL.delete_entire_DLL()
print([node.value for node in DoublyLL ])
print([node for node in DoublyLL])









