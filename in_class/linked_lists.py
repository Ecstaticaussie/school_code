#Creation of a node (element in a linked list)
class Node:
    def __init__(self, value, forward_pointer):
        self.value = value
        self.forward_pointer = forward_pointer

#The linked list class
class Linked_list:
    #The base of a linked list
    def __init__(self, size, values):
        #Check is the size and values make sense
        if size != len(values): raise ValueError("Size given should equal to the length of values")
        self.size = size
        self.head = None
        self.tail = None
        self.create_linked_list(values)
    
    #Creation of the node
    def __add__(self, value, forward_pointer):
        #Update all the keys by increasing each value by 1
        for key in self.linked_list:
            dict_val = self.linked_list[key]
            
            

    #Proper creation of the linked list
    def create_linked_list(self, values):
        #Empty dictionary, not set
        self.linked_list = {}
        #Adding nodes to the beginnig of the set
        for i in range(self.size):
            #Adding of the first node
            if not self.linked_list: self.__add__(self.size-1, values[i], None)
                
            #Adding of the next nodes - these are at the beginning of the linked list
            else: self.__add(self.size-1, values[i], values[i-1])
            #Setting head to the first node
            self.head = self.linked_list[f"{self.size-i}"]

    