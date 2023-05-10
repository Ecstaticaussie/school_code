#creation of a node (element in a linekd list)

class Node:
    def __init__(self, left_pointer=None, right_pointer=None, value=None):
        self.value = value
        self.back_pointer = left_pointer
        self.forward_pointer = right_pointer

#The linked list class
class Linked_list:
    def __init__(self, size, head=None, tail=None):
        self.size = size
        self.head = head
        self.tail = tail