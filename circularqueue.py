class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.items = [None] * size
        self.front = self.rear = -1

        [None,None,None,None,None]
        [None,None,None,None,14]
        [22,None,None,None,14]
        [22,13,-6,None,14]
        [22,13,-6,None,None]
        [None,13,-6,None,None]
        [None,13,-6,9,None]
        [None,13,-6,9,20]

    def enqueue(self, item):
        if (self.rear + 1) % self.size == self.front:
            print("Queue is full")
        elif self.is_empty():
            self.front = self.rear = 0
            self.items[self.rear] = item
        else:
            self.rear = (self.rear + 1) % self.size
            self.items[self.rear] = item

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
        elif self.front == self.rear:
            item = self.items[self.front]
            self.front = self.rear = -1
            return item
        else:
            item = self.items[self.front]
            self.front = (self.front + 1) % self.size
            return item

    def is_empty(self):
        return self.front == -1 and self.rear == -1
