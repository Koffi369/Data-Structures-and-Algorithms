####################### Sorting Algorithms #######################
    
###### Sorting Algorithms

import math 
def Bubble_Sort(List, order = "Ascending"):
    if order == "Ascending":
        num_traversal = len(List)
        num_elmt = len(List)
        
        for j in range(num_traversal -1 ):
            for i in range(num_elmt - 1):
                if List[i]> List[i + 1]:
                    List[i] , List[i + 1] =  List[i + 1], List[i] 
                    # tmp = List[i]
                    # List[i] = List[i + 1]
                    # List[i + 1] = tmp
            num_elmt -= 1   
            # print(List)   
    return List



# lalist = Bubble_Sort([5,9,3,1])

# lalist


# def Slection_Sort(UnSorted, order = "Ascending"):
#     if order == "Ascending":
#         Sorted = []
#         # UnSorted = List
        
#         while len(UnSorted) != 0:
#             mini = UnSorted[0]
#             mini_idx = 0
#             for i in range(1, len(UnSorted)):            
#                 if UnSorted[i]<mini:
#                     mini = UnSorted[i]
#                     mini_idx = i
            
#             UnSorted[0] , UnSorted[mini_idx] = UnSorted[mini_idx] , UnSorted[0]
            
#             Sorted.append(UnSorted[0])
#             UnSorted = UnSorted[1:]
#             print(Sorted, UnSorted)
#     return Sorted



def Slection_Sort(List, order = "Ascending"):
    if order == "Ascending":
        for last_mini_idx in range(len(List)-1):
            # mini = List[last_mini_idx]
            for j in range(last_mini_idx + 1, len(List)):
                if  List[last_mini_idx] > List[j]: 
                    List[last_mini_idx] , List[j] =  List[j ], List[last_mini_idx]
                    
            print(List)
    return List
        


# lalist = Slection_Sort([2,1,7,6,5,3,4,9,8])

# lalist





# https://www.youtube.com/watch?v=R_wDA-PmGE4&list=PLliXbzY3XhUSJy3izXH-0ojiT3Uup8xbu
def Insertion_Sort(List, order = "Ascending"):
    if order == "Ascending":
        for unsorted_idx in range(1,len(List)): 
            picked_elmt = List[unsorted_idx]
            for sorted_idx in range(unsorted_idx):
                if List[sorted_idx] >  picked_elmt:
                   List[sorted_idx] , List[unsorted_idx] = List[unsorted_idx], List[sorted_idx]
    return List
                


# lalist = Insertion_Sort([2,1,7,6,5,3,4,9,8])

# lalist


def Bucket_Sort(List, order = "Ascending"):
    if order == "Ascending":
        Num_Buckets = round(math.sqrt(len(List)))
        
        All_Buckets = { num:[] for num in range(1,Num_Buckets + 1)}
        
        for i in range(len(List)):
            appropriate_Bucket = math.ceil(List[i]* Num_Buckets/max(List))
            All_Buckets[appropriate_Bucket].append(List[i])
            
        for i in range(1,Num_Buckets + 1):
            All_Buckets[i] =  Insertion_Sort(All_Buckets[i])
            
        res = All_Buckets[1]
        
        for i in range(2,Num_Buckets + 1):
            res =  res + All_Buckets[i]
            
            
    return res

            
# lalist = Bucket_Sort([2,1,7,6,5,3,4,9,8])

# lalist    


# https://www.youtube.com/watch?v=cVZMah9kEjI

def Merge_Sort(Arr, order = "Ascending"):
    if order == "Ascending":
        
        if len(Arr)<=1:
            return Arr
        
        left_Arr = Arr[:len(Arr)//2]
        right_Arr = Arr[len(Arr)//2:]
        
        left_Arr = Merge_Sort(left_Arr)
        right_Arr = Merge_Sort(right_Arr)
        
        # while len(Arr)>1:
        #     left_Arr = Merge_Sort(left_Arr)
        #     right_Arr = Merge_Sort(right_Arr)
            
        
        idx_left_Arr = 0
        idx_right_Arr = 0
        idx_Arr = 0
        
        while idx_left_Arr < len(left_Arr) and idx_right_Arr  < len(right_Arr):
            if left_Arr[idx_left_Arr] < right_Arr[idx_right_Arr]:
                Arr[idx_Arr] = left_Arr[idx_left_Arr]
                idx_left_Arr +=1
            else:
                Arr[idx_Arr] = right_Arr[idx_right_Arr]
                idx_right_Arr +=1
            idx_Arr +=1
            
            
        
        while idx_left_Arr < len(left_Arr):
             Arr[idx_Arr] = left_Arr[idx_left_Arr]
             idx_left_Arr +=1
             idx_Arr +=1
             
        while idx_right_Arr  < len(right_Arr): 
            Arr[idx_Arr] = right_Arr[idx_right_Arr]
            idx_right_Arr +=1
            idx_Arr +=1
        
        return Arr
        
            
# lalist = Merge_Sort([2,1,7,6,5,3,4,9,8,10])

# lalist             


# https://www.youtube.com/watch?v=kFeXwkgnQ9U    
# https://www.youtube.com/watch?v=0SkOjNaO1XY&list=PLBZBJbE_rGRV8D7XZ08LK6z-4zPoWzu5H&index=11
def Quick_Sort(Arr,l,r):
    if l >= r:
        return 
    else:
        p = partition(Arr,l,r)
        Quick_Sort(Arr,l,p-1)
        Quick_Sort(Arr,p+1,r)
    
        
        
def partition(Arr,l,r):
    i = l-1
    for j in range(l,r):
        if Arr[j] < Arr[r]:
            i +=1
            Arr[j] , Arr[i] =  Arr[i] , Arr[j] 
    Arr[r] , Arr[i+1 ] = Arr[i+1 ], Arr[r]
    
    return i+1


# def quicksort(arr):
#     qs(arr, 0, len(arr) - 1)

# def qs(arr, l, r):
#     if l >= r:
#         return
#     p = partition(arr, l, r)

#     qs(arr, l, p - 1)
#     qs(arr, p + 1, r)

# def partition(arr, l, r):
#     pivot = arr[r]
#     i = l - 1
#     for j in range(l, r):
#         if arr[j] < pivot:
#             i += 1
#             arr[i], arr[j] = arr[j], arr[i]
#     arr[i + 1], arr[r] = arr[r], arr[i + 1]
#     return i + 1
        


# A = [2,1,7,6,5,3,4,9,8,10]
    
# Quick_Sort(A,0,9)
# print(A)



class Heap:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.List = [None] * self.maxsize
        self.last_used_idx = -1
        
    def __str__(self):
        return " ".join(self.List)
        
    # For minimum heap
    def heapify_insert(self , idx):
        if idx %2 == 0:
            parent_idx = int((idx  -2)/2)
        else:
            parent_idx = int((idx  -1)/2)
        
        # print(self.List[idx] )
        # print(self.List[parent_idx])
        # print(parent_idx)
        if parent_idx >= 0:
            if self.List[idx] > self.List[parent_idx] or parent_idx < 0:
                return       
            else: 
                self.List[idx], self.List[parent_idx] = self.List[parent_idx], self.List[idx]
                self.heapify_insert(parent_idx)
            
        

        
    def insert_elmt(self, value):
        if self.last_used_idx+1  == self.maxsize:
            print("The heap is full")
            return
        self.last_used_idx +=1
        self.List[self.last_used_idx] = value
        self.heapify_insert(self.last_used_idx)
        
  
    def heapify_delete(self , idx):
        left_child_idx = 2*idx + 1
        right_child_idx = 2*idx + 2
        
        if  self.last_used_idx <= left_child_idx:
            return
        
        # print(self.List[left_child_idx])
        # print(self.List[right_child_idx])
        if self.List[left_child_idx] < self.List[right_child_idx]:
            self.List[idx] , self.List[left_child_idx] = self.List[left_child_idx], self.List[idx]
            self.heapify_delete(left_child_idx)
        else:
            self.List[idx] , self.List[right_child_idx] = self.List[right_child_idx], self.List[idx]
            self.heapify_delete(right_child_idx)

        
    def remove_min(self):
        if self.List[0] == None:
            print("The heap is empty")
            return
        
        poped = self.List[0]
        self.List[0] = self.List[self.last_used_idx] 
        self.List[self.last_used_idx]  = None
        self.last_used_idx -= 1
        
        self.heapify_delete(0)
  
        return poped
        

        
def Heap_Sort(arr):
    My_heap = Heap(len(arr))
    for val in arr:
        My_heap.insert_elmt(val)
    for i in range(len(arr)):
        poped = My_heap.remove_min()
        arr[i] = poped
    return arr
        
    
    
        
    
A = [2,1,7,6,5,3,4,9,8,10]  
 
aaa = Heap_Sort(A)       
    
aaa   


























