#######################  Circular Singly Linked List  ##########################

class Node:
    def __init__(self,Node_value = None):
        self.value = Node_value
        self.next_node_reference = None
        


class Circular_Singly_LinledList:
    def __init__(self):
        self.head = None
        self.tail = None
        
        
    def __iter__(self):
        iter_node = self.head
        while iter_node:
            yield iter_node
            # if iter_node == self.head:
            #     break 
            iter_node = iter_node.next_node_reference
            
            if iter_node == self.tail.next_node_reference:
                break
            
            
            
    def create_CircSLL(self, Node_value = None):
        node  = Node(Node_value)
        node.next_node_reference = node
        self.head = node        
        self.tail = node
        
    def insert_in_CircSLL(self,Node_value, location  ):
        if self.head == None :
            return "No elemt in the CircSLL"
        
        else:
            if location == 0:
                New_node  = Node(Node_value)
                New_node.next_node_reference = self.head
                self.head = New_node
                self.tail.next_node_reference = New_node
                
            elif location == -1:
                New_node  = Node(Node_value)
                New_node.next_node_reference = self.tail.next_node_reference
                self.tail.next_node_reference = New_node
                self.tail = New_node
                           
            else:
                New_node  = Node(Node_value)
                idx = 0
                iter_node = self.head
                while idx < location -1:
                    iter_node = iter_node.next_node_reference
                    idx +=1
                New_node.next_node_reference = iter_node.next_node_reference
                iter_node.next_node_reference = New_node
               
    
    def traverse_CircSLL(self):
        if self.head == None:
            print("The is nothing in the Circular SLL")
        else:
            iter_node = self.head
            while iter_node != self.tail:
                print(iter_node.value)
                iter_node = iter_node.next_node_reference
            print(self.tail.value)
                   
    def search_element_CircSLL(self, value_to_find):
        if self.head == None:
            print("The is nothing in the Circular SLL")
        else:
            iter_node = self.head
            idx = 0
            while iter_node.value != value_to_find  :
                if iter_node == self.tail:
                    return print("element not found ")
                    
                else:                    
                    iter_node = iter_node.next_node_reference
                    idx +=1
            
            print(f"element found at position {idx}")
            
    def delete_node_CircSLL(self, location):
        if self.head == None:
            print("The is nothing in the Circular SLL")
        else:
            iter_node = self.head             
            if location == 0:
                if iter_node.next_node_reference == iter_node:
                    iter_node.next_node_reference = None
                    self.head = None
                    self.tail = None
                else: 
                    self.head = iter_node.next_node_reference 
                    self.tail.next_node_reference = self.head
                
            elif location == -1:
                if iter_node.next_node_reference == iter_node:
                    iter_node.next_node_reference = None
                    self.head = None
                    self.tail = None
                else:
                    pred_iter_node = self.head
                    while iter_node != self.tail: 
                        pred_iter_node = iter_node
                        iter_node = iter_node.next_node_reference
                    pred_iter_node.next_node_reference = self.head
                    self.tail = pred_iter_node
                           
            else: 
                idx = 0
                pred_iter_node = self.head
                succ_iter_node = self.head
                succ_iter_node = succ_iter_node.next_node_reference
                while idx < location:
                    pred_iter_node = iter_node
                    iter_node = succ_iter_node
                    succ_iter_node = succ_iter_node.next_node_reference
                    idx += 1
                pred_iter_node.next_node_reference = succ_iter_node
                    
                    
    def delete_entire_CircSLL(self):
        if self.head == None:
            print("The is nothing in the Circular SLL")
        else: 
            self.head = None
            self.tail.next_node_reference = None
            self.tail = None


# Video1

# Circ_LL = Circular_Singly_LinledList() 
# Circ_LL.create_CircSLL(5)


# print([ node.value for node in Circ_LL])



# Video4

# Circ_LL = Circular_Singly_LinledList() 
# Circ_LL.create_CircSLL(5)

# Circ_LL.insert_in_CircSLL(3,0)
# Circ_LL.insert_in_CircSLL(7,-1)
# Circ_LL.insert_in_CircSLL("midle1",1)
# Circ_LL.insert_in_CircSLL("midle3",3)
# print([ node.value for node in Circ_LL])


# # Video5

# Circ_LL = Circular_Singly_LinledList() 
# Circ_LL.create_CircSLL(5)

# Circ_LL.insert_in_CircSLL(3,0)
# Circ_LL.insert_in_CircSLL(7,-1)
# Circ_LL.insert_in_CircSLL("midle1",1)
# Circ_LL.insert_in_CircSLL("midle3",3)

# Circ_LL.traverse_CircSLL()



# Video6

# Circ_LL = Circular_Singly_LinledList() 
# Circ_LL.create_CircSLL(5)

# Circ_LL.insert_in_CircSLL(3,0)
# Circ_LL.insert_in_CircSLL(7,-1)
# Circ_LL.insert_in_CircSLL("midle1",1)
# Circ_LL.insert_in_CircSLL("midle3",3)

# Circ_LL.search_element_CircSLL(7)



# Video9  Deleting a node

# Circ_LL = Circular_Singly_LinledList() 
# Circ_LL.create_CircSLL(5)

# Circ_LL.insert_in_CircSLL(3,0)
# Circ_LL.insert_in_CircSLL(7,-1)
# Circ_LL.insert_in_CircSLL("midle1",1)
# Circ_LL.insert_in_CircSLL("midle3",3)
# print([ node.value for node in Circ_LL])

# Circ_LL.delete_node_CircSLL(-1)

# print([ node.value for node in Circ_LL])





# Video 10   Deleting entire CSLL

Circ_LL = Circular_Singly_LinledList() 
Circ_LL.create_CircSLL(5)

Circ_LL.insert_in_CircSLL(3,0)
Circ_LL.insert_in_CircSLL(7,-1)
Circ_LL.insert_in_CircSLL("midle1",1)
Circ_LL.insert_in_CircSLL("midle3",3)
print([ node.value for node in Circ_LL])

Circ_LL.delete_entire_CircSLL()

print([ node.value for node in Circ_LL])





















