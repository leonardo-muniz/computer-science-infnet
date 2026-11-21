class Stack:

    def __init__(self, capacity):

        self.capacity = capacity
        self.data = [None] * capacity
        self.top = -1

    def push(self, value):

        if self.top == self.capacity - 1:
            raise OverflowError("Stack overflow")

        self.top += 1
        self.data[self.top] = value

    def pop(self):

        if self.top == -1:
            raise IndexError("Stack underflow")

        value = self.data[self.top]

        self.top -= 1

        return value

    def state(self):
        return self.data