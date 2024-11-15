
# -*- coding: utf-8 -*-
"""
DSA Learning Draft
"""

import numpy as np

def g(n):
    # X = 
    if  n == 1:
        return np.array([0,1])
    else:
        return np.concatenate((g(n-1) , np.array([10**(n-1) + i for i in g(n-1)])))

g(4)


#######################  Linked List  ##########################

class Node:
    def __init__(self, value = None):
        self.value = value
        self.next_node_reference = None

class Linked_list:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next_node_reference
            
    def insert_node(self, value , location):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        elif location == 0:
            new_node.next_node_reference = self.head
            self.head = new_node
        elif location == -1:
            new_node.next_node_reference = None
            self.tail.next_node_reference = new_node
            self.tail = new_node 
        else:
            iter_node = self.head
            idx = 0
            while idx < location - 1:
                iter_node = iter_node.next_node_reference
                idx +=1
            temp = iter_node.next_node_reference
            iter_node.next_node_reference = new_node
            new_node.next_node_reference = temp
            
    
    def traverse_list(self):
        if self.head == None:
            return "Nothing in the list"
        else:
            iter_node = self.head
            # while iter_node.next_node_reference != None:
            while iter_node != None:
                print(iter_node.value)
                iter_node = iter_node.next_node_reference
        
    def search_element(self, elmt):
        if self.head == None:
            return "Nothing in the list"
        else:
            iter_node = self.head
            idx = 0
            while iter_node != None:
                if iter_node.value == elmt:
                    return f"{elmt} found at positiion {idx}"
                    break
                else:
                    iter_node = iter_node.next_node_reference
                    idx += 1
            if iter_node == None and idx != 0:
                print("elemnt not found")
            
                
        

"""
# Video 6
llist = Linked_list()

Node1 = Node()
Node2 = Node()


llist.head = Node1 

llist.head.next_node_reference = Node2

llist.tail = Node2

"""



"""
# Video 8 

llist = Linked_list()         
llist.insert_node(1,-1)
llist.insert_node(2,-1)
llist.insert_node(3,-1)
#insert an element at the beginning   
llist.insert_node('elmt_begin',0)    
#insert an element in the midle   
llist.insert_node('elmt_midle',3)       
print([node.value for node in llist])    

"""


# # Video 9

# llist = Linked_list()         
# llist.insert_node(1,-1)
# llist.insert_node(2,-1)
# llist.insert_node(3,-1)
# #insert an element at the beginning   
# llist.insert_node('elmt_begin',0)    
# #insert an element in the midle   
# llist.insert_node('elmt_midle',3)  
# llist.insert_node(4,-1)
# print([node.value for node in llist])
# llist.traverse_list()


# Video 10

llist = Linked_list()         
llist.insert_node(1,-1)
llist.insert_node(2,-1)
llist.insert_node(3,-1)
#insert an element at the beginning   
llist.insert_node('elmt_begin',0)    
#insert an element in the midle   
llist.insert_node('elmt_midle',3)  
llist.insert_node(4,-1)
print([node.value for node in llist])
llist.search_element(3)










































































































