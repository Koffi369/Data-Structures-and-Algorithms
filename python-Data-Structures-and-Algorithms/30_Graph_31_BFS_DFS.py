####################### Graph Algorithms & Graph Traversal #######################
    
###### Graph

class Node:
    def __init__(self, node_value):
        self.value = node_value
        self.next_node_reference = None
        
    def __str__(self):
        return str(self.value)
    
    
class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def __iter__(self):
        iter_node = self.head 
        while iter_node:
            yield iter_node
            iter_node = iter_node.next_node_reference


class Queue:
    def __init__(self):
        self.queue = Linked_List()
        
    def __str__(self):
        values = [str(x) for x in self.queue]
        return " ".join(values)
    
    
    def isEmpty(self):
        if self.queue.head == None:
            return True
        return False
         
        
    def enqueue(self, value):
        # print("enqueue", value)
        new_node = Node(value)
        # print(new_node)
        if self.isEmpty() == True:
            # print('Here')
            self.queue.head = new_node
            self.queue.tail = new_node
            
        else:
            self.queue.tail.next_node_reference = new_node
            self.queue.tail = new_node
        # print("sucess enqueue",value)
        return 
            
            
    def dequeue(self):
        if self.isEmpty() == True:
            print("The queue is Empty")
            return
        else:     
            # poped = self.queue.head.value
            poped = self.queue.head
            if self.queue.tail == self.queue.head:
                self.queue.head = None
                self.queue.tail = None
            else:
                self.queue.head = self.queue.head.next_node_reference
            return poped
            # poped = self.queue.head.value
            # print("type poped  11",type(poped))
            # print("type poped.value  11",type(poped.value))
            # self.queue.head = self.queue.head.next_node_reference
            # return poped
   



class Stack:
    def __init__(self):
        self.stack = Linked_List()
        
    def __str__(self):
        values = [str(x) for x in self.stack]
        return " ".join(values)
    
    
    def isEmpty(self):
        if self.stack.head == None:
            return True
        return False   
     
        
    def push(self,elmt):
        new_node = Node(elmt)
        if self.isEmpty() == True:
            self.stack.head = new_node
            self.stack.tail = new_node
        else:
            new_node.next_node_reference = self.stack.head
            self.stack.head = new_node
            
    def pop(self):
        if self.isEmpty() == True:
            print("the stack is empty")
            return
        
        poped = self.stack.head
        if self.stack.head  ==  self.stack.tail:
            self.stack.head = None
            self.stack.tail = None
        else:
            self.stack.head = self.stack.head.next_node_reference
            
        return poped
            
     

    
class Graph:
    def __init__(self,graph_dict = None):
        if graph_dict == None:
            graph_dict = {}
        self.graph_dict = graph_dict
            
    def __str__(self):
        return str(self.graph_dict)
    
    def isEmpty(self):
        if self.graph_dict == {}:
            print("The Graph is empty")
            return True
        return False
    
    

    def add_Edge(self, vertex, Edge):
        # print("HOLL1")
        if vertex in self.graph_dict:            
            self.graph_dict[vertex].append(Edge)     
        else:
            self.graph_dict[vertex] = [Edge]
            
         
    def BFS(self):
        if self.isEmpty() == True:
            return
        dict_queue = Queue()
        first_key = next(iter(self.graph_dict))
        dict_queue.enqueue(first_key)
        visited = []
        
        while dict_queue.isEmpty() == False:
            poped = dict_queue.dequeue()
            
            if poped.value not in visited:
                visited.append(poped.value)
                print("poped.value", poped.value)
                
                for adjacent_Node in self.graph_dict[poped.value]:   
                    if adjacent_Node not in visited:
                        print(adjacent_Node)
                        dict_queue.enqueue(adjacent_Node)
                print("_______")
        print(visited)

        


    def DFS(self):
        first_key = next(iter(self.graph_dict))
        graph_stack = Stack()

        graph_stack.push(first_key) 
        visited = []
        
        while graph_stack.isEmpty() == False:

            poped = graph_stack.pop()
            
            # print("graph_stack", graph_stack)
            
            # break
            print("poped", poped)
            
            
            if poped.value not in visited:
                visited.append(poped.value)
                # print("visited", visited)
                for adjacent_Node in self.graph_dict[poped.value]:
                    if adjacent_Node not in visited:
                        graph_stack.push(adjacent_Node)
                        print("pushed", adjacent_Node)
                    
                print("_______")
        print(visited)     
        
        
        
        
     
            
        
      




# Video 5 (Chap 30) Creation of a graph:
# My_Graph = Graph()

# print(My_Graph)
# My_Graph.add_Edge("a","b")

# print(My_Graph)

# My_Graph.add_Edge("a","b2")

# print(My_Graph)


# Video 1 (Chap 31) BFS 




graph_dict = { "a" : ["b","c"],
            "b" : ["a", "d", "g"],
            "c" : ["a", "d", "e"],
            "d" : ["b", "c", "f"],
            "e" : ["c", "f"],
            "f" : ["e","d", "g"] ,
            "g" : ["b", "f"] }


My_Graph = Graph(graph_dict)

My_Graph.DFS()




























