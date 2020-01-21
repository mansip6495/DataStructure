class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class single_linkedlist:
    def __init__(self):
        self.head = None

    def add_node(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node

    def search_node(self,data):
        temp = self.head
        while temp is not None:
            if temp.data == data:
                print("Node exists")
                break
            else:
                temp = temp.next
        if temp is None:
            print("Node not found")

    def delete_node(self,data):

        if self.head.data == data:
            self.head = self.head.next
        else:
            temp = self.head
            while temp.next is not None:
                if temp.next.data == data:
                    temp.next = temp.next.next
                    break
                else:
                    temp = temp.next


    def print_linkedlist(self):
        temp = self.head
        while temp is not None:
            print(temp.data,end='->')
            temp = temp.next



if __name__ == '__main__':
    linked_list = single_linkedlist()

    for i in range(6):
        linked_list.add_node(i)

    linked_list.print_linkedlist()
    linked_list.search_node(7)
    linked_list.delete_node(2)
    linked_list.print_linkedlist()