#######################  Doubly Linked List  ##########################

class Node:
    def __init__(self, node_value = None):
        self.value = node_value
        self.next_node_reference = None
        self.prev_node_reference = None



class Doubly_Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def __iter__(self):
        node = self.head
        while node:
            yield node
            
            if node == self.tail:
                break
            node = node.next_node_reference
        
    def Create_DLL(self,node_value):
        New_node = Node(node_value)
        self.tail = New_node
        self.head = New_node
        
        



DoublyLL= Doubly_Linked_List()

DoublyLL.Create_DLL(5)

print([node.value for node in DoublyLL ])













