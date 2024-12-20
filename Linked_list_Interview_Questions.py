##### Video 1 Linked List Class 

from random import randint  

class Node():
    def __init__(self, node_value = None):
        self.value = node_value
        self.next_node_reference = None
        self.prev_node_reference = None
        
    def __str__(self):
        return str(self.value)
        
        
class Linked_List():
    def __init__(self):
        self.head = None
        self.tail = None
        
        
    def __iter__(self):
        iter_node = self.head
        while iter_node != self.tail:
            yield iter_node
            iter_node = iter_node.next_node_reference
        yield self.tail

    def __str__(self):
        LL_values = [str(x.value) for x in self]
        return ' -> '.join(LL_values)
        
        
    def __len__(self):
        iter_node = self.head
        cnt = 0
        while iter_node != self.tail:
            iter_node = iter_node.next_node_reference
            cnt += 1
        cnt += 1
        return cnt
    
    def add(self, node_value = None):
        New_node = Node(node_value)
        if self.head == None:
            self.head = New_node
            self.tail = New_node
        else:
            self.tail.next_node_reference = New_node
            self.tail = New_node
            
    def generate_LL(self, num_elmts, min_value , max_value):
        self.head = None
        self.tail = None
        
        for i in range(num_elmts):
            node_value = randint(min_value , max_value)
            self.add(node_value)
        return self
    
    
    ##############################       Video 2 
    '''
    Question 1:
    Write a code to remove duplicates from an unsorted Linked List
    '''
            
    
    def remove_duplicates(self):
        
        print(" ######  All Duplicates will be removed   ######")
        # iter_node = self.head
        # Value_list = []
        # Value_list.append(iter_node.value)
        
        # while iter_node != self.tail:
        #     if  iter_node.next_node_reference.value in Value_list:
        #         iter_node.next_node_reference = iter_node.next_node_reference.next_node_reference                
        #         print(Value_list)
        #     else:
        #         Value_list.append(iter_node.next_node_reference.value)
        #         iter_node = iter_node.next_node_reference   
         
        prev_iter_node = self.head
        iter_node = prev_iter_node.next_node_reference
        Value_list = []
        Value_list.append(prev_iter_node.value)
        
        while iter_node != self.tail:
            if iter_node.value in Value_list:
                prev_iter_node.next_node_reference = iter_node.next_node_reference
                iter_node = iter_node.next_node_reference
            else:
                Value_list.append(iter_node.value)
                prev_iter_node = iter_node
                iter_node = iter_node.next_node_reference
        if prev_iter_node.value == iter_node.value:
            self.tail = prev_iter_node
            
        
        
        
        
    ##############################       Video 3 
    '''
    Question 2:
    Implement  and algorithm to find the n-th to last element of a Singly Linked List
    '''               
    # def return_nth_to_last(self, n_th):
    #     if self.head == None:
    #         return "There is nothing in the LL"
    #     else:
    #         iter_node = self.head
    #         idx = 1
    #         while  idx < n_th:
    #             iter_node = iter_node.next_node_reference
    #             self.head = iter_node
    #             idx += 1
                
    # def return_n_last_elmts(self, n):
    #     if self.head == None:
    #         return "There is nothing in the LL"
    #     else:
    #         iter_node = self.head
    #         begining = len(self) - n +1
    #         idx = 1
    #         while  idx < begining:
    #             iter_node = iter_node.next_node_reference
    #             self.head = iter_node
    #             idx += 1
                
    # def return_nth_elmt_from_last(self, n):
    #     if self.head == None:
    #         return "There is nothing in the LL"
    #     else:
    #         iter_node = self.head
    #         begining = len(self) - n +1
    #         idx = 1
    #         while  idx < begining:
    #             iter_node = iter_node.next_node_reference
    #             idx += 1
            
    #         return  iter_node.value
    
    
    def return_nth_elmt_from_last(self, n):
        if self.head == None:
            return "There is nothing in the LL"
        else:
            pt_iter_node = self.head
            pt_nth_elemt = self.head
            idx1 = 0
            idx2 = 0
            
            while pt_iter_node.next_node_reference: 
                #va aller jusqu'a self.tail
                pt_iter_node = pt_iter_node.next_node_reference
                idx1 += 1
                if idx1 - idx2 == n:
                    pt_nth_elemt = pt_nth_elemt.next_node_reference
                    idx2 += 1
            if n-1 > idx1:
                # print(idx1)
                return "Your input is larger than the linked list size"
            
            return pt_nth_elemt.value
                
  
    
  
    ##############################       Video 4
    '''
    Question 3:
    write a code to partition a linked list around a value x, such that all nodes less than
    x come before all nodes greater than or equal to x.
    '''  
    
    def partition(self, x):
        # Let's find x
        x_node = self.head
        while x_node.value != x:
            if x_node == self.tail:
                break
            x_node = x_node.next_node_reference
        
        iter_node = self.head
        
        while iter_node != self.tail:
            if iter_node.value > x_node.value:
                temp = iter_node.value
                iter_node.value = x_node.value 
                x_node.value  = temp
                x_node.next_node_reference = iter_node.next_node_reference  
            iter_node = iter_node.next_node_reference
                
                
            
        
        while iter_node != self.tail:
            if iter_node.value < x_node.value:
                temp = iter_node.value
                iter_node.value = x_node.value 
                x_node.value  = temp
                x_node.next_node_reference = iter_node.next_node_reference             
            iter_node = iter_node.next_node_reference    
    
    
    
  
##### Video 1
        
# My_LL = Linked_List() 

# My_LL.generate_LL(10, 0, 99)   

# print(My_LL)  
# len(My_LL)


##### Video 2

# My_LL = Linked_List() 
# My_LL.add(1)
# My_LL.add(2)
# My_LL.add(1)
# My_LL.add(4)
# My_LL.add(2)
# My_LL.add(3)
# My_LL.add(2)
# My_LL.add(4)
# My_LL.add(5)

# print(My_LL)  
# print(len(My_LL))
   
# My_LL.remove_duplicates()
# print(My_LL)  
# print(len(My_LL))         

##### Video 3

# My_LL = Linked_List() 

# My_LL.add("head")
# My_LL.add(1)
# My_LL.add(2)
# My_LL.add(3)
# My_LL.add(4)
# My_LL.add(5)

# print(My_LL)     
# print(My_LL.return_nth_elmt_from_last(4))


##### Video 4

My_LL = Linked_List() 

My_LL.add(11)
My_LL.add(3)
My_LL.add(9)
My_LL.add(10)
My_LL.add(15)

My_LL.partition(10)

print(My_LL) 

































