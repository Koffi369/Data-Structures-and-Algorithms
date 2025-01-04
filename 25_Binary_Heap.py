####################### AVL Tree #######################
    
###### Creation of Binary Heap

class Binary_Heap_Node:
    def __init__(self, max_size):
        self.max_size = max_size
        self.List = [None] * self.max_size
        self.size_of_heap = -1
        
    # def __str__(self):
    #     return 
        
        
             
def peek_of_heap(root_node):
    if root_node.List[0] == None:
        print("The Heap is empty")
        return
    elif root_node==None:
        print("The Heap doesn't exist")
        return
    else: 
        return root_node.List[0]


def size_of_heap(root_node):
    if root_node==None:
        print("The Heap doesn't exist")
        return
    
    return root_node.size_of_heap      


def LevelOrder_traversal(root_node):
    # print("Holla")
    if root_node.List[0] == None:
        print("The Heap is empty")
        return
    elif root_node==None:
        print("The Heap doesn't exist")
        return
    else:
        for i in range(root_node.size_of_heap +1):
            print(root_node.List[i])
            
      
def swap(Binary_Heap, idx1,idx2):
    tmp = Binary_Heap.List[idx1]
    Binary_Heap.List[idx1] = Binary_Heap.List[idx2]
    Binary_Heap.List[idx2] = tmp
            
# def heapify_Insertion(Binary_Heap, idx, Heap_type): 
#     if Heap_type == "min" :           
#         if idx % 2 !=0:
#             parent_idx = (idx - 1)/2
#             while Binary_Heap.List[parent_idx] < Binary_Heap.List[idx] or parent_idx <0:
#                 swap(Binary_Heap , parent_idx, idx)
#                 idx = parent_idx
#                 parent_idx = (idx - 1)/2
#         else:
#             parent_idx = (idx - 2)/2
#             while Binary_Heap.List[parent_idx] < Binary_Heap.List[idx] or parent_idx <0:
#                 swap(Binary_Heap , parent_idx, idx)
#                 idx = parent_idx
#                 parent_idx = (idx - 2)/2
            
                
def heapify_Insertion(Binary_Heap, idx, Heap_type):
    if idx % 2 !=0:
        parent_idx = int((idx - 1)/2)
        # print(parent_idx)
    else:
        parent_idx = int((idx - 2)/2)
        # print(parent_idx)
        
    if parent_idx < 0:
        return
    if Heap_type == "min":
        if Binary_Heap.List[parent_idx] > Binary_Heap.List[idx]:
            swap(Binary_Heap , parent_idx, idx)
            heapify_Insertion(Binary_Heap, parent_idx, Heap_type)
            
    elif Heap_type == "max":
        if Binary_Heap.List[parent_idx] < Binary_Heap.List[idx]:
            swap(Binary_Heap , parent_idx, idx)
            heapify_Insertion(Binary_Heap, parent_idx, Heap_type)   
    else:
        print("incorrect Heap type")
        return
        
    
def insertion_of_Node(Binary_Heap, node_value, Heap_type):
    if Binary_Heap.size_of_heap +1 == Binary_Heap.max_size:
        print("The heap is full")
        return
    Binary_Heap.size_of_heap +=1
    Binary_Heap.List[Binary_Heap.size_of_heap] =  node_value
    heapify_Insertion(Binary_Heap, Binary_Heap.size_of_heap , Heap_type)
    return "Insertion completed"
    
       
    
My_heap =  Binary_Heap_Node(5)

insertion_of_Node(My_heap,4, "max")
# insertion_of_Node(My_heap,0, "max")  
insertion_of_Node(My_heap,5, "max")
insertion_of_Node(My_heap,2, "max")
insertion_of_Node(My_heap,1, "max")  
   
LevelOrder_traversal(My_heap)     
        
        
        
def heapify_Extraction(Binary_Heap, idx, Heap_type):
        Left_child_idx = 2*idx +1 
        Righ_child_idx = 2*idx +2
        if Left_child_idx > Binary_Heap.size_of_heap:
            return

        if Heap_type == "min": 
            
            if Binary_Heap.List[Left_child_idx] < Binary_Heap.List[Righ_child_idx]:
                swap(Binary_Heap , Left_child_idx, idx)
                heapify_Extraction(Binary_Heap, Left_child_idx, Heap_type)
            else:
                swap(Binary_Heap , Righ_child_idx, idx)
                heapify_Extraction(Binary_Heap, Righ_child_idx, Heap_type)

        if Heap_type == "max": 
            
            if Binary_Heap.List[Left_child_idx] > Binary_Heap.List[Righ_child_idx]:
                swap(Binary_Heap , Left_child_idx, idx)
                heapify_Extraction(Binary_Heap, Left_child_idx, Heap_type)
            else:
                swap(Binary_Heap , Righ_child_idx, idx)
                heapify_Extraction(Binary_Heap, Righ_child_idx, Heap_type) 
                
  
                


def Extraction_of_Node(Binary_Heap, Heap_type):   
    Main_root = Binary_Heap.List[0]
    Binary_Heap.List[0] = Binary_Heap.List[Binary_Heap.size_of_heap]
    Binary_Heap.List[Binary_Heap.size_of_heap] = None
    Binary_Heap.size_of_heap -= 1
    heapify_Extraction(Binary_Heap, 0, Heap_type)
    return Main_root
    
    
extracted = Extraction_of_Node(My_heap, "max")
    
print("LevelOrder_traversal(My_heap)    After Extarction")
LevelOrder_traversal(My_heap)        

    
    
def Delete_entire_heap(Binary_Heap):
    Binary_Heap.List = None
    print("Succesfully deleted")
    return
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
        
        
        
        
        
        
        
        
        
        
        


    
    