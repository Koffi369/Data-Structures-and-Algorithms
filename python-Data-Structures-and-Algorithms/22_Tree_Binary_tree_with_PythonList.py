####################### Tree & Binary tree with a Python List #######################
    


    
########### Video 17 Creation of a Binary tree using Python List


class  Binary_Tree_Node:
    def __init__(self, max_size):
        self.max_size = max_size
        self.Binary_Tree = [None] * self.max_size
        self.last_occupied_index = -1
        
        
    def __str__(self):
        values = [str(x) for x in self.Binary_Tree]
        return " ".join(values)
        
    def inserting_a_node(self, value):
        if self.last_occupied_index +1 == self.max_size :
            print("The  tree is full")
            return 
        else:
            self.last_occupied_index +=1
            self.Binary_Tree[self.last_occupied_index ] = value
            
            
    def searching_a_node(self, Node_value):
        for i in range(self.last_occupied_index +1):
            # print(i)
            if self.Binary_Tree[i] == Node_value:
                print(f"{Node_value} found at position {i}")
                return 
            
        print(f"{Node_value} not found")
        return 
    
    
    ########### Video 20 PreOrder traversal

    

    def PreOrder_traversal(self, root_Node_id):        
        # if  root_Node_id > self.max_size - 1:
        if  root_Node_id > self.last_occupied_index:
            return
        
        else:
            print(self.Binary_Tree[root_Node_id])
            self.PreOrder_traversal(2 *root_Node_id +1 )
            self.PreOrder_traversal(2 *root_Node_id +2 )

            
            
    ########### Video 21 InOrder traversal

    

    def InOrder_traversal(self, root_Node_id):     
        # if  root_Node_id > self.max_size - 1:
        if  root_Node_id > self.last_occupied_index:
            return
        
        else:
            
            self.InOrder_traversal(2 *root_Node_id +1 )
            print(self.Binary_Tree[root_Node_id])
            self.InOrder_traversal(2 *root_Node_id +2 )
          
    ########### Video 22 PostOrder traversal

    

    def PostOrder_traversal(self, root_Node_id):
        # if  root_Node_id > self.max_size - 1:
        if  root_Node_id > self.last_occupied_index:
            return
        
        else:
            
            self.PostOrder_traversal(2 *root_Node_id +1 )
            self.PostOrder_traversal(2 *root_Node_id +2 )     
            print(self.Binary_Tree[root_Node_id])
            
            
            
    ########### Video 23 LeveltOrder traversal

    

    def LevelOrder_traversal(self, root_Node_id):
        # Easy way will be by looping but the interesting way will be to use queue
        for i in range(root_Node_id, self.last_occupied_index +1):
            print(self.Binary_Tree[i])
            

    ########### Video 24 Deleting a node
    

    def deleting_a_node(self, root_Node_id):
        if self.last_occupied_index == 0:
            print("the tree is empty")
            return 
        deep = self.Binary_Tree[self.last_occupied_index]
        self.Binary_Tree[root_Node_id] = deep
        
        self.Binary_Tree[self.last_occupied_index] = None
        self.last_occupied_index -= 1
        

    ########### Video 25 Deleting the tree
    

    def deleting_BT(self):
        self.Binary_Tree = None






    
        

My_BT = Binary_Tree_Node(8)
    
My_BT.inserting_a_node("Drinks") 
My_BT.inserting_a_node("Hot") 
My_BT.inserting_a_node("Cold") 

My_BT.inserting_a_node("Tea") 
My_BT.inserting_a_node("Coffee") 
My_BT.inserting_a_node("Fanta")  
My_BT.inserting_a_node("Cola")  
    
print("My_BT ===>>>  ",My_BT)  

# print(My_BT.last_occupied_index)   

# My_BT.searching_a_node("Cold")

# My_BT.PreOrder_traversal(0)
# My_BT.InOrder_traversal(0)
# My_BT.PostOrder_traversal(0)
My_BT.LevelOrder_traversal(0)
        
    
    
    