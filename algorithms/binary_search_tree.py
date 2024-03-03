class Node:
    def __init__(self, data, name) -> None:
        self.data = data
        self.name = name
        self.right = None
        self.left = None

    def __str__(self) -> str:
        return f'({self.name}, {self.data})'


class binary_search_tree:
    def __init__(self) -> None:
        pass

    def insert(self, root, data, name) -> Node:
        node = Node(data, name)

        # root getting initialized for the 1st time or root with same value with different name
        if root is None or root.data == data:
            root = node

        if data < root.data:
            root.left = self.insert(root.left, data, name)
        elif data > root.data:
            root.right = self.insert(root.right, data, name)

        return root

    def _height(self, root):
        if root is None:
            return 0

        leftHeight = self._height(root.left)
        rightHeight = self._height(root.right)

        return leftHeight + 1 if leftHeight > rightHeight else rightHeight + 1

    def _inorder_predecessor(self, root):
        while root is not None and root.right is not None:
            root = root.right

        return root

    def _inorder_successor(self, root):
        while root is not None and root.left is not None:
            root = root.left

        return root

    def delete(self, root, key):

        if root is None:
            return None

        if root.left is None and root.right is None:
            root = None
            return None

        if key < root.data:
            root.left = self.delete(root.left, key)
        elif key > root.data:
            root.right = self.delete(root.right, key)
        else:
            if self._height(root.left) > self._height(root.right):
                node = self._inorder_predecessor(root.left)
                root.data = node.data
                root.left = self.delete(root.left, node.data)
            else:
                node = self._inorder_successor(root.right)
                root.data = node.data
                root.right = self.delete(root.right, node.data)

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


BST = binary_search_tree()
root = None
root = BST.insert(root, 50, 'F')
BST.insert(root, 10, 'B')
BST.insert(root, 40, 'A')
BST.insert(root, 20, 'C')
BST.insert(root, 30, 'D')

print(', '.join(str(node) for node in BST.inorder_traversal(root)))

root = BST.delete(root, 50)
print(', '.join(str(node) for node in BST.inorder_traversal(root)))

root = BST.delete(root, 40)
print(', '.join(str(node) for node in BST.inorder_traversal(root)))

root = BST.delete(root, 30)
print(', '.join(str(node) for node in BST.inorder_traversal(root)))

root = BST.delete(root, 20)
print(', '.join(str(node) for node in BST.inorder_traversal(root)))

root = BST.delete(root, 10)
print(', '.join(str(node) for node in BST.inorder_traversal(root)))
