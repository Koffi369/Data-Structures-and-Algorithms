#######################  Circular Doubly Linked List  ##########################

class Node():
    def __init__(self, node_value = None):
        self.value = node_value 
        self.next_node_reference = None
        self.prev_node_reference = None
        
 
        
class Circular_DLL():
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        iter_node = self.head
        while iter_node != self.tail:
            yield iter_node
            iter_node = iter_node.next_node_reference
        yield iter_node
        
        
    def create_CDLL(self, node_value = None):
        New_node = Node(node_value)
        New_node.next_node_reference = New_node
        New_node.prev_node_reference = New_node
        self.head = New_node
        self.tail = New_node
        
    def insert_node_in_CDLL(self, node_value, location):
        if self.head == None:
            print("Sorry there is nothing in the DLL")
        else:   
            New_node = Node(node_value)
            if location == 0:
                New_node.next_node_reference =  self.head
                self.head.prev_node_reference = New_node
                New_node.prev_node_reference =  self.tail
                self.tail.next_node_reference = New_node
                self.head = New_node
                
            elif location == -1:
                New_node.prev_node_reference = self.tail
                self.tail.next_node_reference = New_node
                New_node.next_node_reference =  self.head
                self.head.prev_node_reference = New_node
                self.tail = New_node
                
            else:
                iter_node = self.head
                idx = 0
                while idx < location -1:
                    iter_node = iter_node.next_node_reference
                    idx += 1
                iter_node.next_node_reference.prev_node_reference = New_node
                New_node.next_node_reference =  iter_node.next_node_reference
                iter_node.next_node_reference = New_node
                New_node.prev_node_reference = iter_node
                
    def traverse_CDLL(self):
        if self.head == None:
            print("Sorry there is nothing in the DLL")
        else:
            iter_node = self.head
            while iter_node != self.tail:
                print(iter_node.value)
                iter_node = iter_node.next_node_reference
            print(iter_node.value)
            
                
                
    def reverse_traverse_CDLL(self):
        if self.head == None:
            print("Sorry there is nothing in the DLL")
        else:
            iter_node = self.tail
            while iter_node != self.head:
                print(iter_node.value)
                iter_node = iter_node.prev_node_reference
            print(iter_node.value)       
            
            
    def search_node_in_CDLL(self, node_value):
        if self.head == None:
            print("Sorry there is nothing in the DLL")
        else:
            iter_node = self.head
            idx = 0
            while iter_node.value != node_value:
                if iter_node == self.tail:
                    return "Element not found in the CDLL"
                iter_node = iter_node.next_node_reference
                idx += 1
            print(f"Element found at index {idx}")
                 
    def delete_node_in_CDLL(self,location):
        if self.head == None:
            print("Sorry there is nothing in the DLL")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.next_node_reference = None
                    self.head.prev_node_reference = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next_node_reference
                    self.head.prev_node_reference = self.tail
                    self.tail.next_node_reference = self.head
                    
            elif location == -1:
                if self.head == self.tail:
                    self.head.next_node_reference = None
                    self.head.prev_node_reference = None
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev_node_reference
                    self.tail.next_node_reference = self.head
                    self.head.prev_node_reference = self.tail
            else:
                iter_node = self.head
                idx = 0
                while  idx < location -1 :
                    iter_node = iter_node.next_node_reference
                    idx += 1
                iter_node.next_node_reference.next_node_reference.prev_node_reference = iter_node
                iter_node.next_node_reference = iter_node.next_node_reference.next_node_reference
                
                
    def delete_entire_CDLL(self):
        if self.head == None:
            print("Sorry there is nothing in the DLL")
        else:
            self.tail.next_node_reference = None
            iter_node = self.head
            while iter_node:
                iter_node.prev_node_reference = None
                iter_node = iter_node.next_node_reference
            self.head = None
            self.tail = None
 
            
            # self.tail.next_node_reference = None
            # iter_node = self.head
            # while iter_node != self.tail:
            #     iter_node.prev_node_reference = None
            #     iter_node = iter_node.next_node_reference
                
                
            # # self.tail.prev_node_reference = None
            # self.tail = None
            # self.head = None
            
        
            
        
                
                
                
  
##### Video 1 Creation of a Circular Doubly LL

# CDLL = Circular_DLL()
# CDLL.create_CDLL(5)
# print([node.value for node in CDLL])


# ##### Video 4 Inserting a node in a Circular Doubly LL

# CDLL = Circular_DLL()
# CDLL.create_CDLL(1)
# print([node.value for node in CDLL])
# CDLL.insert_node_in_CDLL(0, 0)
# CDLL.insert_node_in_CDLL(2,-1)
# CDLL.insert_node_in_CDLL(1.5, 2)

# print([node.value for node in CDLL])


# ##### Video 5 traversal of a Circular Doubly LL

# CDLL = Circular_DLL()
# CDLL.create_CDLL(1)
# print([node.value for node in CDLL])
# CDLL.insert_node_in_CDLL(0, 0)
# CDLL.insert_node_in_CDLL(2,-1) 
# CDLL.insert_node_in_CDLL(1.5, 2)

# print([node.value for node in CDLL])

# CDLL.traverse_CDLL()


# ##### Video 6 reverse traversal of a Circular Doubly LL

# CDLL = Circular_DLL()
# CDLL.create_CDLL(1)
# print([node.value for node in CDLL])
# CDLL.insert_node_in_CDLL(0, 0)
# CDLL.insert_node_in_CDLL(2,-1)
# CDLL.insert_node_in_CDLL(1.5, 2)

# print([node.value for node in CDLL])

# CDLL.reverse_traverse_CDLL()


# ##### Video 7 Search for a node in  a Circular Doubly LL

# CDLL = Circular_DLL()
# CDLL.create_CDLL(1)
# print([node.value for node in CDLL])
# CDLL.insert_node_in_CDLL(0, 0)
# CDLL.insert_node_in_CDLL(2,-1)
# CDLL.insert_node_in_CDLL(1.5, 2)

# print([node.value for node in CDLL])

# CDLL.search_node_in_CDLL(2)





# ##### Video 10 deletion of a node in  a Circular Doubly LL

# CDLL = Circular_DLL()
# CDLL.create_CDLL(1)

# CDLL.insert_node_in_CDLL(0, 0)
# CDLL.insert_node_in_CDLL(2,-1)
# CDLL.insert_node_in_CDLL(1.5, 2)

# print([node.value for node in CDLL])

# CDLL.delete_node_in_CDLL(0)
# print([node.value for node in CDLL])


##### Video 11 deletion of the entire Circular Doubly LL

CDLL = Circular_DLL()
CDLL.create_CDLL(1)

CDLL.insert_node_in_CDLL(0, 0)
CDLL.insert_node_in_CDLL(2,-1)
CDLL.insert_node_in_CDLL(1.5, 2)

print([node.value for node in CDLL])

CDLL.delete_entire_CDLL()
# print([node.value for node in CDLL])
print([node for node in CDLL])
len([node for node in CDLL])


















