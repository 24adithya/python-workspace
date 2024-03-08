class Node:
    def __init__(self, data, height=1) -> None:
        self.data = data
        self.right = None
        self.left = None
        self.height = height

    def __str__(self) -> str:
        return f'({self.data})'


class binary_search_tree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, data) -> Node:
        self.root = self._insert(self.root, data)

    def _insert(self, node, data) -> Node:

        # node getting initialized for the 1st time or node with same value with different name
        if node is None:
            node = Node(data, 1)

        if data < node.data:
            node.left = self._insert(node.left, data)
        elif data > node.data:
            node.right = self._insert(node.right, data)

        return node

    def display(self) -> list:
        result = self._inorder_traversal(self.root)
        # print(', '.join(str(node) for node in result))
        return result

    def _inorder_traversal(self, root, result=None):

        if result is None:
            result = []

        if root is None:
            return result

        self._inorder_traversal(root.left, result)
        result.append(root)
        self._inorder_traversal(root.right, result)

        return result

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

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):

        if node is None:
            return None

        # left node being deleted
        if node.data == key and node.left is None and node.right is None:
            return None

        if key < node.data:
            node.left = self._delete(node.left, key)
        elif key > node.data:
            node.right = self._delete(node.right, key)
        else:
            if self._height(node.left) > self._height(node.right):
                newNode = self._inorder_predecessor(node.left)
                node.data = newNode.data
                node.left = self._delete(node.left, newNode.data)
            else:
                newNode = self._inorder_successor(node.right)
                node.data = newNode.data
                node.right = self._delete(node.right, newNode.data)

        return node


BST = binary_search_tree()
BST.insert(50)
BST.insert(10)
BST.insert(40)
BST.insert(20)
BST.insert(30)

print(', '.join(str(node) for node in BST.display()))

BST.delete(50)
print(', '.join(str(node) for node in BST.display()))

BST.delete(40)
print(', '.join(str(node) for node in BST.display()))

BST.delete(30)
print(', '.join(str(node) for node in BST.display()))

BST.delete(20)
print(', '.join(str(node) for node in BST.display()))

BST.delete(10)
print(', '.join(str(node) for node in BST.display()))
