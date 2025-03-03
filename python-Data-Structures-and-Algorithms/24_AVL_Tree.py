####################### AVL Tree #######################
    
###### Creation of AVL Tree

class AVL_tree_Node:
    def __init__(self, value = None):
        self.data =  value
        self.left_child = None
        self.right_child = None
        self.height = 1
        
        
    def __str__(self):
        return str(self.data)



My_AVL = AVL_tree_Node(0)


print(My_AVL)


###### Traversal of AVL Tree

def preorder_traversal(AVL):
    if AVL == None:
        print("the tre is empty")
        return 
    else:
        print(AVL.data)
        preorder_traversal(AVL.left_child)
        preorder_traversal(AVL.right_child)  
        
        
def inorder_traversal(AVL):
    if AVL == None:
        print("the tre is empty")
        return 
    else:       
        inorder_traversal(AVL.left_child)
        print(AVL.data)
        inorder_traversal(AVL.right_child) 
        
        
def postorder_traversal(AVL):
    if AVL == None:
        print("the tre is empty")
        return 
    else:       
        postorder_traversal(AVL.left_child)
        postorder_traversal(AVL.right_child)   
        print(AVL.data)
        
        
      
        
############################### preliminaries for LevelOrder_traversal      
        

class Node:
    def __init__(self, value):
        self.value = value
        self.next_node_reference = None
        
    def __str__(self):
        return str(self.value)

        
class Linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def __iter__(self):
        iter_node = self.head
        while iter_node:
            yield iter_node
            iter_node = iter_node.next_node_reference
            
    
class queue:
    def __init__(self):
        self.queue = Linkedlist()
        
    def __str__(self):
        values = [ str(x.values) for x in  self.queue]
        return " ".join(values)
    
    def enqueue(self, value):
        new_node = Node(value)
        if self.queue.head == None:
            self.queue.head = new_node
            self.queue.tail = new_node
            
        else:
            self.queue.tail.next_node_reference = new_node
            self.queue.tail = new_node
            
    def dequeue(self):
        if self.queue.head == None:
            print("The Queue is empty")
            return
        else:
            dequeued = self.queue.head
            if  self.queue.head == self.queue.tail:
                self.queue.head = None
                self.queue.tail = None
            else:
                self.queue.head = self.queue.head.next_node_reference
            return dequeued

#######################################################################
        


def levelorder_traversal(AVL):
    if AVL == None:
        print("the tre is empty")
        return 
    else:
        thequeue = queue()
        thequeue.enqueue(AVL)
        while thequeue.queue.head != None:
            dequeued = thequeue.queue.head
            print(dequeued.value.data)
            if dequeued.value.left_child != None:
                dequeued.enqueue(dequeued.value.left_child)
                
            if dequeued.value.right_child != None:
                dequeued.enqueue(dequeued.value.right_child)
            
        
    
def search_a_node(AVL, node_value_to_search):
    if AVL == None:
        print("the tre is empty")
        return 
    else:
        if AVL.data == node_value_to_search:
            return "Found"
        elif node_value_to_search < AVL.data :
            search_a_node(AVL.left_child, node_value_to_search)
        else:
            search_a_node(AVL.right_child, node_value_to_search)
        
    
        
################################### Insertion of a Node in an AVL tree       
        
        
        
def get_height(root_node):
    if root_node == None:
        return 0
    return root_node.height


def Left_Rotation(disbalanced_node):
    New_root = disbalanced_node.right_child
    disbalanced_node.right_child = disbalanced_node.right_child.left_child
    New_root.left_child = disbalanced_node
    
    New_root.height = 1 + max(get_height(New_root.left_child), get_height(New_root.right_child))
    disbalanced_node.height = 1 + max(get_height(disbalanced_node.left_child), get_height(disbalanced_node.right_child))
    
    return New_root
    
        
        
def Right_Rotation(disbalanced_node):
    New_root = disbalanced_node.left_child
    disbalanced_node.left_child = disbalanced_node.left_child.right_child
    New_root.right_child = disbalanced_node
    
    New_root.height = 1 + max(get_height(New_root.left_child), get_height(New_root.right_child))
    disbalanced_node.height = 1 + max(get_height(disbalanced_node.left_child), get_height(disbalanced_node.right_child))
    
    return New_root
    
        
        
def get_balance(root_node):
    return     get_height(root_node.left_child)  - get_height(root_node.right_child) 
        
        
        
        
def inserting_a_node(AVL, node_value):
    if AVL == None:
        AVL = AVL_tree_Node(node_value)
        return AVL
    else:
        if node_value <= AVL.data:
            inserting_a_node(AVL.left_child, node_value)
        else:
            inserting_a_node(AVL.right_child, node_value)
            
    balance = get_balance()
            
            
    
            
        

        
        
        
        
        
        
        
        
        
        
        
        
        


    
    