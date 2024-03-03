class Stack:
    def __init__(self) -> None:
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, data):
        self.items.append(data)

    def pop(self):
        if self.is_empty():
            raise IndexError('Pop from empty stack!')

        item = self.items[-1]
        self.items = self.items[:-1]
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError('Pop from empty stack!')

        return self.items[-1]

    def display(self):
        print(f'\n{self.items}')


stack = Stack()
stack.push(10)
stack.push(20)

stack.display()

print(stack.peek())
print(stack.pop())

stack.display()

print(stack.pop())
stack.display()
print(stack.pop())
