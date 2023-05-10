#creation of a node (element in a linekd list)

class Node:
    def __init__(self, left_pointer=None, right_pointer=None, value=None, at_head=None, at_tail=None):
        self.value = value
        self.back_pointer = left_pointer
        self.forward_pointer = right_pointer

#The linked list class
class Linked_list:
    def __init__(self, size):
        self.size = size
        self.head = None
        self.tail = None