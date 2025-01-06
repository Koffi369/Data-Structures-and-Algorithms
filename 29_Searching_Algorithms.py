####################### Searching Algorithms #######################
    
###### Searching Algorithms

  
def linear_search(arr, elmt):
    for i in range(len(arr)):
        if arr[i] == elmt:
            return i 
    return -1


def Binary_search(arr, elmt):
    # pivot = len(arr)//2
    left = 0
    right = len(arr) -1
    pivot = left + int ((right - left + 1 )//2)
    print(pivot)
    found = False
    
    while left < right:
        if elmt <  arr[pivot]:
            right = pivot
            pivot = right - int ((right - left + 1 )//2)
            
        elif elmt >  arr[pivot]:
            left = pivot
            pivot = left + int ((right - left + 1 )//2)
        else:
            found = True
            print("Element found at index,",pivot)
            return found
            
    return -1
            
            
A = [1,2,3,4,5]  
    
Binary_search(A,-2)  

















































