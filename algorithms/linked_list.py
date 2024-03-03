class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linked_list:

    def __init__(self):
        self.head = None

    def add(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = node

    def display(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

    def delete(self, data):
        previous = None
        current = self.head
        while current is not None:
            if current.data == data:
                print(f'Element found: {current.data}')
                if previous is None:  # handle `head` node deletion
                    self.head = current.next
                else:
                    previous.next = current.next  # change pointers
                current = None
                break
            else:
                previous = current
                current = current.next


list = linked_list()
list.add(10)
list.add(20)
list.add(30)

list.display()
list.delete(20)
list.display()
list.delete(10)
list.display()
list.delete(30)
list.display()
