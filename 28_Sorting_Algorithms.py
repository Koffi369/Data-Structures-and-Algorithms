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


def merge_two_sorted_array(Arr1, Arr2):
    # l1 = len(Arr1)
    # l2 = len(Arr2)
    # merged_arr = []
    # idx1 = 0
    # idx2 = 0  
    
    # if l1 < l2:  
    #     while idx1 < l1:
    #         if Arr1[idx1] < Arr2[idx2]:
    #             merged_arr.append(Arr1[idx1])
    #             idx1 += 1
    #         else:
    #             merged_arr.append(Arr2[idx2])
    #             idx2 += 1   
    #     merged_arr = merged_arr + Arr2[idx2:]
    # else:
    #     while idx2 < l2:
    #         print(idx2,idx1,l2 )
    #         print(Arr1[idx1])
    #         print(Arr2[idx2])
    #         print("KKKKKKKKKKKKKKKKKKKKk")
    #         if Arr1[idx1] < Arr2[idx2]:
    #             merged_arr.append(Arr1[idx1])
    #             idx1 += 1
    #         else:
    #             merged_arr.append(Arr2[idx2])
    #             idx2 += 1
    #     merged_arr = merged_arr + Arr1[idx2:]
    # return merged_arr


def Merge_Sort(List, order = "Ascending"):
    if order == "Ascending":
    #     if len(List) <2:
    #         return List

    #     List1 = List[0 : int(len(List)/2)-1]
    #     List2 = List[int(len(List)/2)-1:]
        
    #     List1 = Merge_Sort(List1)
    #     List2 = Merge_Sort(List2)
            
    # return merge_two_sorted_array(List1, List2)
        
        
        
                

            
lalist = Merge_Sort([2,1,7,6,5,3,4,9,8,10])

lalist             
        
        
        
    
    


























