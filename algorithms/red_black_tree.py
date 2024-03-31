class Node:
    def __init__(self, data, height=1) -> None:
        self.left_child = None
        self.data = data
        self.right_child = None
        self.height = height
        self.color = 'red'  # by default node will

    def __str__(self) -> str:
        return f'{(self.data, self.color)}'


class red_black_tree:
    def __init__(self) -> None:
        self.root = None

    def _rr_rotation(self, node):
        right_child = node.right_child
        right_child_left_child = right_child.left_child

        right_child.left_child = node
        node.right_child = right_child_left_child

        right_child.color = 'black'
        node.color = 'red'

        return right_child

    def _lr_rotation(self, node):
        node_left_child = node.left_child
        node_left_child_right_child = node_left_child.right_child

        node_left_child_right_child_left_child = node_left_child_right_child.left_child
        node_left_child_right_child_right_child = node_left_child_right_child.right_child

        node.left_child = node_left_child_right_child_right_child
        node_left_child.right_child = node_left_child_right_child_left_child

        node_left_child_right_child.right_child = node
        node_left_child_right_child.left_child = node_left_child

        node.color = 'red'
        node_left_child.color = 'red'
        node_left_child_right_child.color = 'black'

        return node_left_child_right_child

    def _rl_rotation(self, node):
        node_right_child = node.right_child
        node_right_child_left_child = node_right_child.left_child

        node_right_child_left_child_right_child = node_right_child_left_child.right_child
        node_right_child_left_child_left_child = node_right_child_left_child.left_child

        node.right_child = node_right_child_left_child_left_child
        node_right_child.left_child = node_right_child_left_child_right_child

        node_right_child_left_child.left_child = node
        node_right_child_left_child.right_child = node_right_child

        node.color = 'red'
        node_right_child.color = 'red'
        node_right_child_left_child.color = 'black'

        return node_right_child_left_child

    def _ll_rotation(self, node):
        left_child = node.left_child
        left_child_right_child = left_child.right_child

        left_child.right_child = node
        node.left_child = left_child_right_child

        left_child.color = 'black'
        node.color = 'red'

        return left_child

    def _recolor(self, node):
        node.color = 'red'
        if node == self.root:
            node.color = 'black'

        node.left_child.color = 'black'
        node.right_child.color = 'black'

        return node

    def is_right_right_red_conflict(self, node) -> bool:
        return (node.right_child and node.right_child.color == 'red'
                and node.right_child.right_child
                and node.right_child.right_child.color == 'red')

    def is_left_left_red_conflict(self, node) -> bool:
        return (node.left_child and node.left_child.color == 'red'
                and node.left_child.left_child
                and node.left_child.left_child.color == 'red')

    def is_right_left_red_conflict(self, node) -> bool:
        return (node.right_child and node.right_child.color == 'red'
                and node.right_child.left_child
                and node.right_child.left_child.color == 'red')

    def is_left_right_red_conflict(self, node) -> bool:
        return (node.left_child and node.left_child.color == 'red'
                and node.left_child.right_child
                and node.left_child.right_child.color == 'red')

    def is_left_uncle_black(self, node) -> bool:
        return node.left_child is None or node.left_child.color == 'black'

    def is_right_uncle_black(self, node) -> bool:
        return node.right_child is None or node.right_child.color == 'black'

    def _insert(self, node, data) -> Node:

        if node == None:
            node = Node(data)
            if self.root == None:
                self.root = node
                self.root.color = 'black'

        if data < node.data:
            node.left_child = self._insert(node.left_child, data)
        elif data > node.data:
            node.right_child = self._insert(node.right_child, data)

        # check color of self with children
        if self.is_right_right_red_conflict(node):
            if self.is_left_uncle_black(node):
                return self._rr_rotation(node)
            else:  # means left uncle is red
                return self._recolor(node)
        elif self.is_right_left_red_conflict(node):
            if self.is_left_uncle_black(node):
                return self._rl_rotation(node)
            else:  # means left uncle is red
                return self._recolor(node)
        if self.is_left_left_red_conflict(node):
            if self.is_right_uncle_black(node):
                return self._ll_rotation(node)
            else:  # means right uncle is red
                return self._recolor(node)
        elif self.is_left_right_red_conflict(node):
            if self.is_right_uncle_black(node):
                return self._lr_rotation(node)
            else:  # means right uncle is red
                return self._recolor(node)
        return node

    def _inorder_predecessor(self, node):
        while node is not None and node.right_child is not None:
            node = node.right_child

        return node

    def _inorder_successor(self, node):
        while node is not None and node.left_child is not None:
            node = node.left_child

        return node

    def _resolve_double_black_left_child(self, node):
        if node.right_child is not None or node.right_child.color == 'black':
            if (node.right_child.left_child and node.right_child.left_child.color == 'red' or
                    node.right_child.right_child and node.right_child.right_child.color == 'red'):
                # rotate
                pass
            elif (node.right_child.left_child is None or node.right_child.left_child.color == 'black' and
                  node.right_child.right_child is None or node.right_child.right_child.color == 'black'):
                # recolor
                node.color = 'black'
                node.right_child.color = 'red'
                return node
        elif node.right_child is not None and node.right_child.color == 'red':
            # rotate - LL
            node_right_child = node.right_child
            node_right_child_left_child = node_right_child.left_child

            node_right_child.left_child = node
            node.right_child = node_right_child_left_child

            node_right_child_left_child.color = 'red'

            if self.is_right_right_red_conflict(node):
                node_right_child.left_child = self._rr_rotation(
                    node)
            elif self.is_right_left_red_conflict(node):
                node_right_child.left_child = self._rl_rotation(
                    node)

            return node_right_child

    def _resolve_double_black_right_child(self, node):
        if node.left_child is not None and node.left_child.color == 'black':
            if (node.left_child.left_child and node.left_child.left_child.color == 'red' or
                    node.left_child.right_child and node.left_child.right_child.color == 'red'):
                # rotate
                pass
            elif (node.left_child.left_child is None or node.left_child.left_child.color == 'black' and
                  node.left_child.right_child is None or node.left_child.right_child.color == 'black'):
                # recolor
                node.color = 'black'
                node.left_child.color = 'red'
                return node
        elif node.left_child is not None and node.left_child.color == 'red':
            # rotate - LL
            node_left_child = node.left_child
            node_left_child_right_child = node_left_child.right_child

            node_left_child.right_child = node
            node.left_child = node_left_child_right_child

            node_left_child_right_child.color = 'red'

            if self.is_left_left_red_conflict(node):
                node_left_child.right_child = self._ll_rotation(
                    node)
            elif self.is_left_right_red_conflict(node):
                node_left_child.right_child = self._lr_rotation(
                    node)

            return node_left_child

    def _delete(self, node, key) -> Node:

        # key not found
        if node is None:
            return

        # leaf node
        if node.data == key and node.left_child is None and node.right_child is None:
            if node == self.root:
                self.root = None

            if node.color == 'red':  # leaf node is red then do nothing
                return None
            else:  # leaf node is black then return `double black` to either recolor or rotate
                return 'double black'

        if key < node.data:
            node.left_child = self._delete(node.left_child, key)
        elif key > node.data:
            node.right_child = self._delete(node.right_child, key)
        else:  # match found

            if node.left_child is not None:
                # by default we are considering `inorder_predecesor`
                new_node = self._inorder_predecessor(node.left_child)
                node.data = new_node.data
                node.left_child = self._delete(node.left_child, new_node.data)

                # if val is None or val == 'double black':
                #     node.left_child = None

                # if val == 'double black':
                #     return self._resolve_double_black_left_child(node)

            else:
                # if left child is not present we are considering `inorder_successor`
                # leaf node condition is already handled in the beginning so either left or right
                # child will always be there
                new_node = self._inorder_successor(node.right_child)
                node.data = new_node.data
                node.right_child = self._delete(
                    node.right_child, new_node.data)

                # if val is None or val == 'double black':
                #     node.right_child = None

                # if val == 'double black':
                #     return self._resolve_double_black_right_child(node)

        if node.left_child == 'double black':
            node.left_child = None
            return self._resolve_double_black_left_child(node)
        elif node.right_child == 'double black':
            node.right_child = None
            return self._resolve_double_black_right_child(node)

        return node

    def insert(self, data) -> Node:
        self.root = self._insert(self.root, data)

    def delete(self, data) -> Node:
        self.root = self._delete(self.root, data)

    def display(self) -> list:
        result = self._inorder_traversal(self.root)
        return result

    def _inorder_traversal(self, root, result=None):

        if result is None:
            result = []

        if root is None:
            return result

        self._inorder_traversal(root.left_child, result)
        result.append(root)
        self._inorder_traversal(root.right_child, result)

        return result


# red_black = red_black_tree()

# red_black.insert(10)
# red_black.insert(20)
# red_black.insert(30)
# red_black.insert(50)
# red_black.insert(40)
# # print(', '.join(str(node) for node in red_black.display()))
# red_black.insert(60)
# red_black.insert(70)
# red_black.insert(80)
# red_black.insert(4)
# red_black.insert(8)

# print(', '.join(str(node) for node in red_black.display()))

# deletion cases

red_black_delete = red_black_tree()
red_black_delete.insert(70)
red_black_delete.insert(40)
red_black_delete.insert(100)
red_black_delete.insert(20)
red_black_delete.insert(50)
red_black_delete.insert(10)
red_black_delete.insert(30)
red_black_delete.insert(60)
red_black_delete.insert(80)
red_black_delete.insert(110)
red_black_delete.insert(90)
red_black_delete.insert(120)

print(', '.join(str(node) for node in red_black_delete.display()))

# red node deletion
red_black_delete.delete(100)
print(', '.join(str(node) for node in red_black_delete.display()))

# red node deletion
red_black_delete.delete(110)
print(', '.join(str(node) for node in red_black_delete.display()))

# black node deletion
red_black_delete.delete(80)
print(', '.join(str(node) for node in red_black_delete.display()))

# red node deletion
red_black_delete.delete(120)
print(', '.join(str(node) for node in red_black_delete.display()))

# black node deletion
red_black_delete.delete(90)
print(', '.join(str(node) for node in red_black_delete.display()))
