class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class circular_linked_list:

    def __init__(self):
        self.head = None

    def add(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            node.next = self.head
        else:
            previous = self.head
            current = previous.next

            while current != self.head:
                previous = current
                current = current.next

            previous.next = node
            node.next = self.head

    def delete(self, data):
        previous = None
        current = self.head

        while current.data != data:
            previous = current
            current = current.next

        print(f'Deleting element {current.data}')

        if previous is None:  # handle head deletion
            if current.next == self.head:  # only 1 node
                self.head = None
            else:
                last_node = self.head
                while last_node.next != self.head:
                    last_node = last_node.next

                last_node.next = self.head.next
                self.head = self.head.next
        else:
            previous.next = current.next
        current = None

    def display(self):
        current = self.head

        if current is None:
            print(f'Empty list')
            return
        print(current.data)
        current = current.next
        while current != self.head:
            print(current.data)
            current = current.next


list = circular_linked_list()
list.add(10)
list.add(20)
list.add(30)
list.add(40)
list.add(50)

list.display()
list.delete(20)
list.display()
list.delete(30)
list.display()
list.delete(40)
list.display()
list.delete(10)
list.display()
