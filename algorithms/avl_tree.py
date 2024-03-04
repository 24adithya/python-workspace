class Node:
    def __init__(self, data, height) -> None:
        self.left = None
        self.data = data
        self.right = None
        self.height = height

    def __str__(self) -> str:
        return f'{self.data}'


class avl_tree:
    def __init__(self) -> None:
        self.root = None

    def _node_height(self, node) -> int:
        left_height, right_height = 0, 0

        if node is not None and node.left is not None:
            left_height = node.left.height

        if node is not None and node.right is not None:
            right_height = node.right.height

        return left_height + 1 if left_height > right_height else right_height + 1

    def _balance_factor(self, node) -> int:
        left_height, right_height = 0, 0
        if node is not None and node.left is not None:
            left_height = node.left.height

        if node is not None and node.right is not None:
            right_height = node.right.height

        return left_height - right_height

    def _ll_rotation(self, node) -> Node:
        node_left_child = node.left
        node_left_child_right = node_left_child.right
        node_left_child.right = node
        node.left = node_left_child_right

        node.height = self._node_height(node)
        node_left_child.height = self._node_height(node_left_child)

        return node_left_child

    def _lr_rotation(self, node) -> Node:
        node_left_child = node.left
        node_left_child_right = node_left_child.right
        node_left_child_right_left_child = node_left_child_right.left
        node_left_child_right_right_child = node_left_child_right.right

        # assign node's left child to point to node's 'child's -> left child
        node_left_child.right = node_left_child_right_left_child

        # make `node_left_child_right` new node by
        # step 1: assign node's left child's right child -> left to point to original node's left child
        node_left_child_right.left = node_left_child

        # step 2: assign node's left child's right child -> right to point to original node
        node_left_child_right.right = node

        # assign node_left_child's right childs' right child to original node's left child
        node.left = node_left_child_right_right_child

        # calculate new heights for original node and new node as well as original node's left child
        node_left_child.height = self._node_height(node_left_child)
        node.height = self._node_height(node)
        node_left_child_right.height = self._node_height(node_left_child_right)

        # finally, return newly assigned node i.e. node's left child's right child
        return node_left_child_right

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

        # update height before returning
        node.height = self._node_height(node)

        if self._balance_factor(node) == 2 and self._balance_factor(node.left) == 1:
            return self._ll_rotation(node)
        elif self._balance_factor(node) == 2 and self._balance_factor(node.left) == -1:
            return self._lr_rotation(node)

        return node

    def display(self) -> list:
        result = self._inorder_traversal(self.root)
        print(', '.join(str(node) for node in result))
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


avl = avl_tree()

avl.insert(10)
avl.insert(5)
avl.insert(2)
# AVL.insert(root, 30, 'D')

print(', '.join(str(node) for node in avl.display()))


avl = avl_tree()
avl.insert(10)
avl.insert(5)
# root = AVL.insert(root, 2)
avl.insert(8)
avl.insert(7)
avl.insert(9)
# root = AVL.insert(root, 6)

print(', '.join(str(node) for node in avl.display()))
