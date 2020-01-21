class Queue():
    def __init__(self,size):
        self.front = 0
        self.rear = 0
        self.queue = [None] * size

    def isempty(self):
        if self.front == self.rear:
            return 1
        else:
            return 0

    def isfull(self):
        if self.rear == len(self.queue):
            return 1
        else:
            return 0

    def enqueue(self,data):
        if self.isfull():
            print("Queue Overflow!")
            return
        else:
            self.queue[self.rear] = data
            self.rear += 1

    def dequeue(self):
        if self.isempty():
            print("Queue is empty!")
            return
        else:
            element = self.queue[self.front]
            self.front += 1
            return element

    def print_front(self):
        if self.isempty():
            print("Queue is empty!")
        else:
            print(self.queue[self.front])

    def print_queue(self):
        print(self.queue)

if __name__ == '__main__':
    q = Queue(5)
    q.print_queue()
    q.dequeue()
    for i in range(4):
        q.enqueue(i)
    q.print_queue()
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    q.print_front()