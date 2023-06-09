class Stack:
    def __init__(self):
        self.stack = []

    def push(self, elem): self.stack.append(elem)

    def pop(self, elem): self.stack.pop(elem)