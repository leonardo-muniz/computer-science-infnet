class Queue:

    def __init__(self, capacity):

        self.capacity = capacity
        self.data = [None] * capacity

        self.front = 0
        self.rear = 0

        self.size = 0

    def enqueue(self, value):

        if self.size == self.capacity:
            raise OverflowError(
                "Queue overflow"
            )

        self.data[self.rear] = value

        self.rear = (
            self.rear + 1
        ) % self.capacity

        self.size += 1

    def dequeue(self):

        if self.size == 0:
            raise IndexError(
                "Queue underflow"
            )

        value = self.data[self.front]

        self.front = (
            self.front + 1
        ) % self.capacity

        self.size -= 1

        return value