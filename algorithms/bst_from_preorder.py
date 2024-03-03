class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.right = None
        self.left = None

    def __str__(self) -> str:
        return f'{self.data}'

# [30,20,10,15,25,40,50,45]


def create_bst(list) -> Node:
    if list is None or len(list) == 0:
        return list
    i = 0
    stack, root, node = [], None, None
    '''
        base condition when stack is empty. This can happen when root element is popped out and
        comparison occurs with stack's top element
    '''
    stack.append(Node(float('inf')))

    while i < len(list):
        if i == 0:
            node = Node(list[i])
            root = node
            i = i + 1

        if list[i] < node.data:
            '''
                If item is less than current node's data, simply create a node to the left 
                of the current node and push the item to the stack. Move node pointer to its left
            '''
            stack.append(node)
            temp = Node(list[i])
            node.left = temp
            node = node.left

            i = i + 1

        elif list[i] > node.data and list[i] < stack[-1].data:
            '''
                If item is greater than current node's data and less than stack's top element,
                create a node and assign the right of current node to the new element and move 
                node pointer
            '''
            temp = Node(list[i])
            node.right = temp
            node = node.right
            i = i + 1
        else:
            '''
                Item doesn't lie in range i.e. less than node's data as well as greater than stack's 
                top element, then pop top element and point node to that element
            '''
            node = stack.pop()

    return root


def inorder_traversal(root, result=None):

    if result is None:
        result = []

    if root is None:
        return result

    inorder_traversal(root.left, result)
    result.append(root.data)
    inorder_traversal(root.right, result)

    return result


root = create_bst([30, 20, 10, 15, 25, 40, 50, 45])
print(inorder_traversal(root))
