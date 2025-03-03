####################### Trie #######################
    
###### Creation of Trie



class Trie_Node:
    def __init__(self):
        self.children = {}    #to map characters to their next Node
        self.end_of_string = False   # to indicate if the node is a end of string or not

class Trie:
    def __init__(self):
        self.root = Trie_Node()
        
        
    def Insert_word(self, word):
        
        iter_node = self.root
        for char in word:   
            node_linked_to_char = iter_node.children.get(char)
            if node_linked_to_char == None:
                new_node = Trie_Node()
                iter_node.children.update({char:new_node})
                iter_node = new_node
            else:
                iter_node = node_linked_to_char
        iter_node.end_of_string = True
        print("Successfully inserted")
        
        
        
        
    def Searching_a_word(self, word):
        iter_node = self.root
        for char in word:   
            node_linked_to_char  = iter_node.children.get(char)
            if node_linked_to_char == None:
                print(f"The word {word} is not in the Trie")
                return False
            else:
                iter_node = node_linked_to_char
        if iter_node.end_of_string == True:
            print(f"The word {word} is  in the Trie")
            return  True
        else:
            print(f"The word {word} is not in the Trie")
            return False
                
               
def Deleting_a_word(Root_Node, word):    
     
        
        
        
 
        
        
        
        
        
        
        
        
        
        
        
                

# Video 3 Insertion of word
My_Trie = Trie() 

My_Trie.Insert_word("APPO")

My_Trie.Insert_word("APPL")

print(My_Trie.root.children["A"].children["P"].children["P"].children)
print(My_Trie.root.end_of_string)

    
    
My_Trie.Searching_a_word("APPLO")
    

    
    
    
    
    
    
    