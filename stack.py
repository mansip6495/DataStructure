class Stack():
    def __init__(self,size):
        self.top = 0
        self.stack = [None]*size

    def is_empty(self):
        if self.top == 0:
            return 1
        else:
            return 0

    def is_full(self):
        if self.top == len(self.stack):
            return 1
        else:
            return 0

    def push(self,data):
        if self.is_full():
            print("Stack overflow!")
            return
        else:
            self.stack[self.top] = data
            self.top += 1
            print("Element added to stack")

    def pop(self):
        if self.is_empty():
            print("Stack is empty!")
            return
        else:
            self.top -= 1
            top = self.stack[self.top]
            self.stack[self.top]=None
            return top

    def top_element(self):
        return self.stack[self.top-1]

    def print_stack(self):
        print(self.stack)

if __name__ == '__main__':
    s = Stack(5)
    for i in range(4):
        s.push(i)
    s.pop()
    print(s.top_element())