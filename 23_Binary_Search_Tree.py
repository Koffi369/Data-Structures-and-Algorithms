####################### Binary Search Tree #######################
    


############ Video 2 Creation of a BST

class BST_Node:
    def __init__(self, Node_value):
        self.data = Node_value
        self.left_child = None
        self.right_child = None
        
        

############ Video 3 Insertion of a new Node
        
def inserting_a_Node(BST, New_node): 
    if New_node.data  <= BST.data : 
        if BST.left_child == None:
            BST.left_child = New_node
            return 
        else:
            inserting_a_Node(BST.left_child, New_node)
    else:
        if BST.right_child == None:
            BST.right_child = New_node
            return 
        else:
            inserting_a_Node(BST.right_child, New_node)
     
    print("The new node has been successfully inserted")
    return 


My_BST = BST_Node(70)

n50 = BST_Node(50)
n90 = BST_Node(90)
n30 = BST_Node(30)
n60 = BST_Node(60)
n80 = BST_Node(80)
n100 = BST_Node(100)
n20 = BST_Node(20)
n40 = BST_Node(40)


inserting_a_Node(My_BST, n50 )
inserting_a_Node(My_BST, n90)
inserting_a_Node(My_BST, n30 )
inserting_a_Node(My_BST, n60 )
inserting_a_Node(My_BST, n80 )
inserting_a_Node(My_BST, n100)
inserting_a_Node(My_BST, n20)
inserting_a_Node(My_BST, n40)

print("My_BST.left_child.data",My_BST.left_child.data)







############ Video 4 Traverse a BST

def PreOrder_traversal(BST):
    if BST  == None:
        return
    else:
        print(BST.data)
        PreOrder_traversal(BST.left_child)
        PreOrder_traversal(BST.right_child)
        


def InOrder_traversal(BST) :
    if BST  == None:
        return
    else:      
        InOrder_traversal(BST.left_child)
        print(BST.data)
        InOrder_traversal(BST.right_child)
    

    
    
    
def PostOrder_traversal(BST) :
    if BST  == None:
        return
    else:      
        PostOrder_traversal(BST.left_child)
        PostOrder_traversal(BST.right_child) 
        print(BST.data)
        

            
        
############################### preliminaries for LevelOrder_traversal

class node:
    def __init__(self, value):
        self.value = value
        self.next_node_reference = None
        
    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.tail = None
        self.head = None
        
    def __iter__(self):
        iter_node = self.head
        while iter_node:
            yield iter_node
            iter_node = iter_node.next_node_reference
    
    
class Queue:
    def __init__(self):
        self.queue = LinkedList()
        
    def __str__(self):
        values = [str(x.value) for x in self.queue]
        return " ".join(values)
        
    def enqueue(self, node_value):
        a_node = node(node_value)
        if self.queue.head == None:          
            self.queue.head = a_node
            self.queue.tail = a_node
        else:
            self.queue.tail.next_node_reference = a_node
            self.queue.tail = a_node
            
            
    def dequeue(self):
        if self.queue.head == None: 
            print("The Queue is empty")
            return
        else:
            dequeed = self.queue.head
            self.queue.head = self.queue.head.next_node_reference
            return dequeed
     
#####################################################################

def LevelOrder_traversal(BST):
    if BST  == None:
        return
    else:
        new_queue = Queue()
        new_queue.enqueue(BST)
        while  new_queue.queue.head != None: 
            root = new_queue.dequeue()
            print (root.value.data)
            if root.value.left_child != None: 
                new_queue.enqueue(root.value.left_child)
                
            if root.value.right_child != None: 
                new_queue.enqueue(root.value.right_child)
    print("LevelOrder_traversal Completed")
                
                



# PreOrder_traversal(My_BST)
# print("PreOrder_traversal Completed")
# InOrder_traversal(My_BST)
# print("InOrder_traversal Completed")
# PostOrder_traversal(My_BST)
# print("PostOrder_traversal Completed")
# LevelOrder_traversal(My_BST)



############ Video 5 searching in a BST

def searching_a_node(BST, NodeValue_to_search):
    if BST  == None:
        print("The Tree is empty")
        return
    else:
        if NodeValue_to_search == BST.data:
            print(f"Node with value {NodeValue_to_search} Found")
            return
        elif NodeValue_to_search < BST.data:
            searching_a_node(BST.left_child, NodeValue_to_search)
            
        else:
            searching_a_node(BST.right_child, NodeValue_to_search)


searching_a_node(My_BST, 60)


############ Video 6 deleting a BST


def find_min_NodeValue_in_right_subtree(BST):
    min_Node = BST
    while  min_Node.left_child != None:
        min_Node = min_Node.left_child
    return min_Node
    
    


       
# def deleting_a_node(BST, NodeValue_to_delete):
#     if BST == None:
#         return
#     else:
#         if BST.data == NodeValue_to_delete:
#             if BST.left_child == None:    
#                 BST = BST.right_child
                
#             elif BST.right_child == None:
#                 BST = BST.left_child
                
#             else:
#                 min_Node = find_min_NodeValue_in_right_subtree(BST.right_child)
#                 BST.right_child = deleting_a_node(BST.right_child, min_Node.data)
#                 BST.data = min_Node.data
#         elif NodeValue_to_delete < BST.data:
#             deleting_a_node(BST.left_child, NodeValue_to_delete)
#         else:
#             deleting_a_node(BST.right_child, NodeValue_to_delete)
            

"""
Always Return in the base case in case of recursion

if you do not modify BST it will still the same
"""    
       
def deleting_a_node(BST, NodeValue_to_delete):
    if BST == None:
        return
    else:
        if BST.data == NodeValue_to_delete:
            if BST.left_child == None:    
                tmp = BST.right_child
                BST = None
                return tmp
                
            elif BST.right_child == None:
                tmp = BST.left_child
                BST = None
                return tmp
                
            else:
                min_Node = find_min_NodeValue_in_right_subtree(BST.right_child)
                BST.right_child = deleting_a_node(BST.right_child, min_Node.data)
                BST.data = min_Node.data
        elif NodeValue_to_delete < BST.data:
            # deleting_a_node(BST.left_child, NodeValue_to_delete)
            BST.left_child = deleting_a_node(BST.left_child, NodeValue_to_delete)
        else:
            # deleting_a_node(BST.right_child, NodeValue_to_delete)
            BST.right_child = deleting_a_node(BST.right_child, NodeValue_to_delete)
    return BST



    
My_BST = deleting_a_node(My_BST,20)   

# My_BST = My_BST.left_child
# LevelOrder_traversal(My_BST)    

# searching_a_node(My_BST, 70)
LevelOrder_traversal(My_BST) 
    

def delete_BST(BST):
    BST.data = None
    BST.left_child = None
    BST.right_child = None
    return "the BST was deleted"
    
    
    
    
    











    
    