class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class circular_linkedlist:
    def __init__(self):
        self.head = None

    def add_node(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.head.next = self.head
        else:
            temp = self.head
            while temp.next is not self.head:
                temp = temp.next
            new_node.next= self.head
            temp.next = new_node

    def search(self,data):
        temp = self.head

        if self.head.data == data:
            print("Node found")
        else:
            temp = self.head.next
            while temp is not self.head:
                if temp.data == data:
                    print("Node Found")
                    break
                else:
                    temp = temp.next
        if temp == self.head:
            print("Node not found")

    def delete_node(self,data):
        temp = self.head
        while temp.next is not self.head:
            if temp.next.data == data:
                temp.next = temp.next.next
                break
            else:
                temp = temp.next
        if self.head.data == data and self.head.next == self.head:
            self.head = None
        elif self.head.data == data:
            while temp.next is not self.head:
                temp = temp.next
            temp.next = self.head.next
            self.head = self.head.next


    def print_linkedlist(self):
        if self.head is None:
            print("Empty List")
            return None
        temp = self.head
        print(temp.data,end='->')
        temp = temp.next

        while temp is not self.head:
            print(temp.data,end='->')
            temp = temp.next
        print(temp.data)

if __name__ == '__main__':
    linked_list = circular_linkedlist()
    linked_list.print_linkedlist()
    for i in range(6):
        linked_list.add_node(i)
    linked_list.print_linkedlist()
    linked_list.search(6)
    linked_list.delete_node(2)
    linked_list.print_linkedlist()
    linked_list.delete_node(1)
    linked_list.print_linkedlist()
    for i in range(6):
        linked_list.delete_node(i)
        linked_list.print_linkedlist()