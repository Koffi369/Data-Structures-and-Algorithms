
# # https://www.geeksforgeeks.org/insertion-sort-algorithm/
# def insertion_sort(Array):
#     for i in range(1,len(Array)):
#         j = i - 1
#         while Array[j]>Array[j+1] and j>=0 :
#             temp = Array[j]
#             Array[j] = Array[j+1]
#             Array[j+1] = temp
#             j -=1
#     return Array




# Arr = [23, 1, 10, 5, 2]


# insertion_sort(Arr)


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
               
                   
                    
                
            






# Video1

# Circ_LL = Circular_Singly_LinledList() 
# Circ_LL.create_CircSLL(5)


# print([ node.value for node in Circ_LL])



# Video4

Circ_LL = Circular_Singly_LinledList() 
Circ_LL.create_CircSLL(5)

Circ_LL.insert_in_CircSLL(3,0)
Circ_LL.insert_in_CircSLL(7,-1)
Circ_LL.insert_in_CircSLL("midle1",1)
Circ_LL.insert_in_CircSLL("midle3",3)
print([ node.value for node in Circ_LL])



































# class Node:
#     def __init__(self, value = None):
#         self.value = value
#         self.next_node_reference = None

# class Linked_list:
#     def __init__(self):
#         self.head = None
#         self.tail = None
        
#     def __iter__(self):
#         node = self.head
#         while node:
#             yield node
#             node = node.next_node_reference
            
#     def insert_node(self, value , location):
#         new_node = Node(value)
#         if self.head == None:
#             self.head = new_node
#             self.tail = new_node
#         elif location == 0:
#             new_node.next_node_reference = self.head
#             self.head = new_node
#         elif location == -1:
#             new_node.next_node_reference = None
#             self.tail.next_node_reference = new_node
#             self.tail = new_node 
#         else:
#             iter_node = self.head
#             idx = 0
#             while idx < location - 1:
#                 iter_node = iter_node.next_node_reference
#                 idx +=1
#             temp = iter_node.next_node_reference
#             iter_node.next_node_reference = new_node
#             new_node.next_node_reference = temp
            
    
#     def traverse_list(self):
#         if self.head == None:
#             return "Nothing in the list"
#         else:
#             iter_node = self.head
#             # while iter_node.next_node_reference != None:
#             while iter_node != None:
#                 print(iter_node.value)
#                 iter_node = iter_node.next_node_reference
        
#     def search_element(self, elmt):
#         if self.head == None:
#             return "Nothing in the list"
#         else:
#             iter_node = self.head
#             idx = 0
#             while iter_node != None:
#                 if iter_node.value == elmt:
#                     return f"{elmt} found at positiion {idx}"
#                     break
#                 else:
#                     iter_node = iter_node.next_node_reference
#                     idx += 1
#             if iter_node == None and idx != 0:
#                 print("elemnt not found")
                
#     def delete_node(self, location):
#         #Assume location starts from 0
#         if self.head == None:
#             return "Nothing in the list"
#         elif location == 0:
#             first_node = self.head.next_node_reference
#             print(self.head.value)
#             print(first_node.value)
            
#             if first_node.next_node_reference == None: #only one node
#                 self.head.next_node_reference = None
#                 self.tail.next_node_reference = None
                
#             else:
#                 self.head = first_node
                
                   
#         elif location == -1:
#             first_node = self.head.next_node_reference

            
#             if first_node.next_node_reference == None: #only one node
#                 self.head.next_node_reference = None
#                 self.tail.next_node_reference = None
#             else:
#                 iter_node = self.head
#                 iter_node_pred = self.head

#                 while iter_node.next_node_reference != None:
#                     iter_node_pred = iter_node
#                     iter_node = iter_node.next_node_reference
                    
#                 iter_node_pred.next_node_reference = None
#                 self.tail.next_node_reference = iter_node_pred
                   
#         else:
#             iter_node = self.head
#             iter_node_pred = self.head
#             idx = 0
#             while idx != location:
#                 iter_node_pred = iter_node
#                 iter_node = iter_node.next_node_reference
#                 idx += 1
                
#             iter_node_succ = iter_node.next_node_reference
            
#             iter_node_pred.next_node_reference = iter_node_succ
            
#     def delete_all(self):
#         self.head = None
#         self.tail = None
            
    





# # Video 11

# llist = Linked_list()         
# llist.insert_node(1,-1)
# llist.insert_node(2,-1)
# llist.insert_node(3,-1)
# llist.insert_node(4,-1)
# #insert an element at the beginning   
# llist.insert_node(0,0)    
# # #insert an element in the midle   
# # llist.insert_node('elmt_midle',3)  
# llist.insert_node(0,4)
# print([node.value for node in llist])
# llist.delete_node(3)
# print([node.value for node in llist])


































































































