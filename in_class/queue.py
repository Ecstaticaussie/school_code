#creation of the queue class
class Queue:
    def __init__(self, max_size):
        #attributes of the queue
        self.max_size = max_size
        self.current_size = 0
        self.queue = [None] * max_size
        self.front_pointer = 0

    #Checks if it is empty
    def is_empty(self):
        for i in self.queue:
            if i != None: False
        return True

    #Checks if it is full
    def is_full(self):
        for i in self.queue:
            if i == None: False
        return True

    #Adding elements -> enqueue
    def enqueue(self, elem):
        #Checks if it is full
        if self.isfull(): print("The queue is full."); return
        #Checks if the element is None -> adds to the front
        for i in range(len(self.queue)):
            if self.queue[i] != None:
                self.queue[i] = elem
                self.front_pointer += 1

    #Removing elements -> Dequeue
    def dequeue(self, elem):
        #Checks if the queue is empty
        if self.isempty(): print("The queue is empty"); return
        #Checks if the element is there -> Removes it
        for i in reversed(range(len(self.queue))):
            if self.queue[i] != None:
                self.queue[i] = None
                self.front_pointer -= 1



