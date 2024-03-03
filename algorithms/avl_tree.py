class Node:
    def __init__(self, data, height) -> None:
        self.left = None
        self.data = data
        self.right = None
        self.height = height

    def __str__(self) -> str:
        return f'{self.data}'


class AVL:
    def __init__(self) -> None:
        pass

    def _height(self, root):
        if root is None:
            return 0

        leftHeight = self._height(root.left)
        rightHeight = self._height(root.right)

        return leftHeight + 1 if leftHeight > rightHeight else rightHeight + 1

    def insert(self, root, data, name) -> Node:

        # root getting initialized for the 1st time or root with same value with different name
        if root is None:
            node = Node(data, name)
            root = node

        if data < root.data:
            root.left = self.insert(root.left, data, name)
        elif data > root.data:
            root.right = self.insert(root.right, data, name)

        return root

    def inorder_traversal(self, root, result=None):

        if result is None:
            result = []

        if root is None:
            return result

        self.inorder_traversal(root.left, result)
        result.append(root)
        self.inorder_traversal(root.right, result)

        return result


AVL = AVL()

root = None
root = AVL.insert(root, 50, 'F')
AVL.insert(root, 10, 'B')
AVL.insert(root, 40, 'A')
AVL.insert(root, 20, 'C')
AVL.insert(root, 30, 'D')

print(', '.join(str(node) for node in AVL.inorder_traversal(root)))
