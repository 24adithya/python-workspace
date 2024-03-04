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

    def _node_height(self, root) -> int:
        left_height, right_height = 0, 0

        if root is not None and root.left is not None:
            left_height = root.left.height

        if root is not None and root.right is not None:
            right_height = root.right.height

        return left_height + 1 if left_height > right_height else right_height + 1

    def balance_factor(self, root) -> int:
        left_height, right_height = 0, 0
        if root is not None and root.left is not None:
            left_height = root.left.height

        if root is not None and root.right is not None:
            right_height = root.right.height

        return left_height - right_height

    def ll_rotation(self, root) -> Node:
        root_left_child = root.left
        root_left_child_right = root_left_child.right
        root_left_child.right = root
        root.left = root_left_child_right

        root.height = self._node_height(root)
        root_left_child.height = self._node_height(root_left_child)

        return root_left_child

    def lr_rotation(self, root) -> Node:
        root_left_child = root.left
        root_left_child_right = root_left_child.right
        root_left_child_right_left_child = root_left_child_right.left
        root_left_child_right_right_child = root_left_child_right.right

        # assign root's left child to point to root's 'child's -> left child
        root_left_child.right = root_left_child_right_left_child

        # make `root_left_child_right` new root by
        # step 1: assign root's left child's right child -> left to point to original root's left child
        root_left_child_right.left = root_left_child

        # step 2: assign root's left child's right child -> right to point to original root
        root_left_child_right.right = root

        # assign root_left_child's right childs' right child to original root's left child
        root.left = root_left_child_right_right_child

        # calculate new heights for original root and new root as well as original root's left child
        root_left_child.height = self._node_height(root_left_child)
        root.height = self._node_height(root)
        root_left_child_right.height = self._node_height(root_left_child_right)

        # finally, return newly assigned root i.e. root's left child's right child
        return root_left_child_right

    def insert(self, root, data) -> Node:

        # root getting initialized for the 1st time or root with same value with different name
        if root is None:
            node = Node(data, 1)
            root = node

        if data < root.data:
            root.left = self.insert(root.left, data)
        elif data > root.data:
            root.right = self.insert(root.right, data)

        # update height before returning
        root.height = self._node_height(root)

        if self.balance_factor(root) == 2 and self.balance_factor(root.left) == 1:
            return self.ll_rotation(root)
        elif self.balance_factor(root) == 2 and self.balance_factor(root.left) == -1:
            return self.lr_rotation(root)

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
root = AVL.insert(root, 10)
root = AVL.insert(root, 5)
root = AVL.insert(root, 2)
# AVL.insert(root, 30, 'D')

print(', '.join(str(node) for node in AVL.inorder_traversal(root)))

root = None
root = AVL.insert(root, 10)
root = AVL.insert(root, 5)
# root = AVL.insert(root, 2)
root = AVL.insert(root, 8)
root = AVL.insert(root, 7)
root = AVL.insert(root, 9)
# root = AVL.insert(root, 6)

print(', '.join(str(node) for node in AVL.inorder_traversal(root)))
