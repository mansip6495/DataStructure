class circularQueue():

    def __init__(self,size):
        self.front = 0
        self.rear = 0
        self.count = 0
        self.queue = [None] * size

    def isempty(self):
        if self.count == 0:
            return 1
        else:
            return 0

    def isfull(self):
        if self.count == len(self.queue):
            return 1
        else:
            return 0

    def enqueue(self,data):
        if self.isfull():
            print("Queue is full!")
        else:
            self.queue[self.rear] = data
            self.rear = (self.rear + 1) % len(self.queue)
            self.count += 1

    def dequeue(self):
        if self.isempty():
            print("Queue is empty")
        else:
            self.queue[self.front] = None
            self.front = (self.front + 1) % len(self.queue)
            self.count -= 1

    def print_queue(self):
        print(self.queue)


if __name__ == '__main__':
    q = circularQueue(5)
    q.print_queue()
    for i in range(6):
        q.enqueue(i)

    q.print_queue()

    for i in range(6):
        q.dequeue()
    q.print_queue()
