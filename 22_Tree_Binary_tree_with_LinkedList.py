####################### Tree & Binary tree using Linked List  #######################
    


    
########### Video 4 Create a Basic tree in python


# class TreeNode:
#     def __init__(self, data, children = []):
#         self.data = data
#         self.children = children
        
        
#     def __str__(self, level = 0):
#         ret = "   " * level + str('.' +self.data) + "\n"
#         for child in self.children:
#             ret += child.__str__(level+1)
#         return ret
    
#     def addChild(self, TreeNode):
#         self.children.append(TreeNode)



# My_tree = TreeNode("Drinks", [])



# Hot = TreeNode("Hot", [])
# Cold = TreeNode("Cold", [])



# Tea = TreeNode("Tea", [])
# Coffee = TreeNode("Coffee", [])


# Fanta = TreeNode("Fanta", [])
# Cola = TreeNode("Cola", [])



########### Video 8 Create a Binary tree using Linked List

class Binary_tree_Node:
    def __init__(self,data):
        self.data = data
        self.left_child = None
        self.right_child = None
        
        
    def __str__(self):
        return str(self.data)
    
    
My_Binary_tree = Binary_tree_Node("Drinks")  


Hot = Binary_tree_Node("Hot")
Cold = Binary_tree_Node("Cold")


My_Binary_tree.left_child = Hot
My_Binary_tree.right_child = Cold

#############

Tea = Binary_tree_Node("Tea")
Coffee = Binary_tree_Node("Coffee")


Hot.left_child = Tea
Hot.right_child = Coffee


#############

Fanta = Binary_tree_Node("Fanta")
Cola = Binary_tree_Node("Cola")


Cold.left_child = Fanta
Cold.right_child = Cola
    

########### Video 9 PreOrder traversal

print(" >>>>>> PreOrder traversal >>>>>> " )

def PreOrder_traversal(Tree_Node):
    if  Tree_Node == None:
        return 
    print(Tree_Node.data)
    PreOrder_traversal(Tree_Node.left_child)
    PreOrder_traversal(Tree_Node.right_child)
    


PreOrder_traversal(My_Binary_tree)


########### Video 10: Inorder traversal

print(" >>>>>> InOrder traversal >>>>>> " )

def InOrder_traversal(Tree_Node):
    if  Tree_Node == None:
        return 
    InOrder_traversal(Tree_Node.left_child)
    print(Tree_Node.data)
    InOrder_traversal(Tree_Node.right_child)
    


InOrder_traversal(My_Binary_tree)

########### Video 11: Postorder traversal

print(" >>>>>> PostOrder traversal >>>>>> " )

def PostOrder_traversal(Tree_Node):
    if  Tree_Node == None:
        return 
    PostOrder_traversal(Tree_Node.left_child)
    PostOrder_traversal(Tree_Node.right_child)
    print(Tree_Node.data)
    


PostOrder_traversal(My_Binary_tree)

########### Video 12: Levelorder traversal



class Node:
    def __init__(self, node_value):
        self.value = node_value
        self.next_node_reference = None
        
    def __str__(self):
        return str(self.value)
    
    
    
class LinkedList:
    def __init__(self):
        self.head  =  None
        self.tail = None
        
    def __iter__(self):
        iter_node = self.head
        while iter_node:
            yield iter_node
            iter_node = iter_node.next_node_reference
    
    
    
class Queue:
    def __init__(self):
        self.queue = LinkedList()
        
        
    def isEmpty(self):
        if self.queue.head == None:
            return True
        else:
            return False
 
        
    def enqueue(self, node_value):
        New_node = Node(node_value)
        
        if self.isEmpty():
            self.queue.head = New_node
            self.queue.tail = New_node
            
        else:
            self.queue.tail.next_node_reference = New_node
            self.queue.tail = New_node
                
                
    def dequeue(self):   
        if self.isEmpty():
            return "The Queue is Empty"     
        else:
            dequeued = self.queue.head.value
            if self.queue.head == self.queue.tail:
                self.queue.head = None
                self.queue.tail = None
            else:
                self.queue.head = self.queue.head.next_node_reference
            return dequeued
                
        
        
        
                
print(" >>>>>> LevelOrder traversal >>>>>> " )          
        
        
def LevelOrder_traversal(Tree_Node):
    if  Tree_Node == None:
        return 
    
    else:
        new_queue = Queue()
        new_queue.enqueue(Tree_Node)
    
        while new_queue.isEmpty() == False:
            curr_root = new_queue.dequeue()
            print(curr_root.data)
            if curr_root.left_child != None:
                new_queue.enqueue(curr_root.left_child)
            if curr_root.right_child != None:
                new_queue.enqueue(curr_root.right_child)
            

 
LevelOrder_traversal(My_Binary_tree)  



########### Video 13 Searching for a Node in a Binary Tree

print(" >>>>>> Searching for a Node >>>>>> " )    

def searching_node(Tree_Node, Node_to_find):
    # print(type(Tree_Node))
    
    if  Tree_Node == None:
        return 
    
    else:

        new_queue = Queue()
        new_queue.enqueue(Tree_Node)
        idx = 1
        while new_queue.isEmpty() == False:
            curr_root = new_queue.dequeue()
            if curr_root.data == Node_to_find.data:
                print(f'Node found in the tree at index {idx}')
                return
            if curr_root.left_child != None:
                new_queue.enqueue(curr_root.left_child)
            if curr_root.right_child != None:
                new_queue.enqueue(curr_root.right_child)
            idx += 1
        print("Node not found in the Tree")
        return "Node not found in the Tree"
    
      
not_founded = Binary_tree_Node("not_founded")

searching_node(My_Binary_tree, Coffee)

searching_node(My_Binary_tree, not_founded)


########### Video 14 Inserting a Node in a Binary Tree

print(" >>>>>> Inserting a Node >>>>>> " )    

def inserting_node(Binary_Tree, Node_to_insert):
    if  Binary_Tree == None:
        print("The tree is empty")
        Binary_Tree = Node_to_insert        
        return 
    
    else:
        new_queue = Queue()
        new_queue.enqueue(Binary_Tree)
    
        while new_queue.isEmpty() == False:
            curr_root = new_queue.dequeue()
            # print(curr_root.data)
            if curr_root.left_child != None:
                new_queue.enqueue(curr_root.left_child)
            else:
                curr_root.left_child = Node_to_insert
                print("Inserted on the  left")
                return 
                
            if curr_root.right_child != None:
                new_queue.enqueue(curr_root.right_child)   
            else:
                curr_root.right_child = Node_to_insert
                print("Inserted on the  right")
                return 
    
    
    
Black_tea = Binary_tree_Node("Black_tea")  
Green_tea = Binary_tree_Node("Green_tea")  
    
inserting_node(My_Binary_tree, Black_tea)   
inserting_node(My_Binary_tree, Green_tea) 
    
LevelOrder_traversal(My_Binary_tree)    
    
    
    
    
    
    
    
########### Video 15 Deleting a Node in a Binary Tree

print(" >>>>>> Deleting a Node >>>>>> " )    

# def deleting_node(Binary_Tree, Node_to_delete):
#     if  Binary_Tree == None:
#         print("The tree is empty")
#         return 
    
#     else:
#         new_queue = Queue()
#         new_queue.enqueue(Binary_Tree)
    
#         while new_queue.isEmpty() == False:
#             curr_root = new_queue.dequeue()
#             # print(curr_root.data)
#             if curr_root.left_child != None:
#                 new_queue.enqueue(curr_root.left_child)
#             if curr_root.right_child != None:
#                 new_queue.enqueue(curr_root.right_child)
#     print(f"{Node_to_delete.data} was deleted and replaced by {curr_root.data}")
#     Node_to_delete.data = curr_root.data
#     curr_root.left_child = None
#     curr_root.right_child = None
#     curr_root.data = None
    
    

    
# deleting_node(My_Binary_tree, Tea) 
    
# LevelOrder_traversal(My_Binary_tree)  
    
    
def get_deepest_node(Binary_Tree):
    if  Binary_Tree == None:
        print("The tree is empty")
        return 
    
    else:
        new_queue = Queue()
        new_queue.enqueue(Binary_Tree)
    
        while new_queue.isEmpty() == False:
            curr_root = new_queue.dequeue()
            # print(curr_root.data)
            if curr_root.left_child != None:
                new_queue.enqueue(curr_root.left_child)
            if curr_root.right_child != None:
                new_queue.enqueue(curr_root.right_child) 
    return curr_root

    
# deep = get_deepest_node(My_Binary_tree)  
# print( deep )
    
    
def delete_deepest_node(Binary_Tree, deepest_node):
    if  Binary_Tree == None:
        print("The tree is empty")
        return 
    
    else:
        new_queue = Queue()
        new_queue.enqueue(Binary_Tree)
    
        while new_queue.isEmpty() == False:
            curr_root = new_queue.dequeue()
            # print(curr_root.data)
            if curr_root.left_child != None:
                if curr_root.left_child == deepest_node:
                    curr_root.left_child = None
                    return
                else:
                    new_queue.enqueue(curr_root.left_child)
            if curr_root.right_child != None:
                if curr_root.right_child == deepest_node:
                    curr_root.right_child = None
                    return
                else:
                    new_queue.enqueue(curr_root.right_child)  
                

            
 

# delete_deepest_node(My_Binary_tree, deep)                
# LevelOrder_traversal(My_Binary_tree)   

              
def deleting_node(Binary_Tree, Node_to_delete):
    if  Binary_Tree == None:
        return 
    
    else:
        new_queue = Queue()
        new_queue.enqueue(Binary_Tree)
        
        deepest_node = get_deepest_node(Binary_Tree)   
            
        delete_deepest_node(Binary_Tree, deepest_node) 
    
        while new_queue.isEmpty() == False:
            curr_root = new_queue.dequeue()
            # print(curr_root.data)
            if curr_root.data ==  Node_to_delete.data:
                # print(Node_to_delete.data)
                # print(curr_root.data)
                temp = curr_root.data
                # print(deepest_node.data)
                curr_root.data = deepest_node.data
                return f"{temp} was deleted and replaced by {deepest_node.data}"
            
            if curr_root.left_child != None:
                new_queue.enqueue(curr_root.left_child)
            if curr_root.right_child != None:
                new_queue.enqueue(curr_root.right_child)
                
        return f"{Node_to_delete.data} is not in this Tree"
    
    
    
print(deleting_node(My_Binary_tree, Fanta))

LevelOrder_traversal(My_Binary_tree)    
    
    
    
    
########### Video 16 Deleting the entire Binary Tree

print(" >>>>>> Deleting the entire Binary Tree >>>>>> " )   


def deleting_the_tree(Binary_Tree):
    if  Binary_Tree == None:
        return 
    
    else:
        print(f"the tree {Binary_Tree} was Deleted ")
        Binary_Tree.data = None
        Binary_Tree.left_child = None
        Binary_Tree.right_child = None
        
        return
    
    
    
    
    
deleting_the_tree(My_Binary_tree)
    
LevelOrder_traversal(My_Binary_tree)    
    
    
    
    
    
    
    
    