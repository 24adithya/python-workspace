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
        if (node.right_child and node.right_child.color == 'red'
            and node.right_child.right_child
            and node.right_child.right_child.color == 'red'
            and (node.left_child is None
                 or node.left_child.color == 'black')):
            return self._rr_rotation(node)
        elif (node.left_child and node.left_child.color == 'red'
              and node.left_child.left_child
              and node.left_child.left_child.color == 'red'
              and (node.right_child is None
                   or node.right_child.color == 'black')):
            #
            return self._ll_rotation(node)
        elif (node.left_child and node.left_child.color == 'red'
              and node.right_child and node.right_child.color == 'red'
              and (node.right_child.right_child and node.right_child.right_child.color == 'red'
                   or node.left_child.left_child and node.left_child.left_child.color == 'red')):
            # if parent and uncle are 'red' then recolor for red-red conflict for recently inserted node
            return self._recolor(node)

        return node

    def insert(self, data) -> Node:
        self.root = self._insert(self.root, data)

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


red_black = red_black_tree()

red_black.insert(10)
red_black.insert(20)
red_black.insert(30)
red_black.insert(50)
red_black.insert(40)

print(', '.join(str(node) for node in red_black.display()))
