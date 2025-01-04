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

def Quick_Sort(Arr, order = "Ascending"):
    if order == "Ascending": 
        if len(Arr)<=1:
            return Arr
        pivot_id = len(Arr) -1
        j = len(Arr) -2
        i = 0
        
        while i < pivot_id and j > 0:
            if Arr[i] > Arr[pivot_id] and Arr[j] < Arr[pivot_id]:
                Arr[j] , Arr[i] = Arr[i], Arr[j]
                i +=1
                j-=1
            else:
                if Arr[i] > Arr[pivot_id]:
                    pass
                else:
                    i+=1
                    
                if Arr[j] < Arr[pivot_id]:
                    pass
                else:
                    j-=1

            if i<=j:
                Arr[pivot_id] , Arr[i]= Arr[i], Arr[pivot_id]
                Arr[:i] = Quick_Sort( Arr[:i])
                Arr[i+1:] = Quick_Sort( Arr[i+1:])    
    
    return Arr
        
    
        
        
    
    
lalist = Quick_Sort([2,1,7,6,5,3,4,9,8,10])

print(lalist    )
    
    
 
        
    
    


























