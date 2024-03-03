
#             30
#           /   \
#          20     40
#         / \     /\
#        15  25   n 50
#       /\  / \    / \
#      10 n n 27  45  n
#          /\  /\  /\
#          n n n n n

class Node:
    def __init__(self, name, data) -> None:
        self.data = data
        self.name = name
        self.left = None
        self.right = None

    def __str__(self) -> str:
        return f'Node with name: {self.name} and value: {self.data}'


F = Node('F', 30)  # root
B = Node('B', 20)
G = Node('G', 40)
A = Node('A', 15)
D = Node('D', 25)
I = Node('I', 50)
C = Node('C', 10)
E = Node('E', 27)
H = Node('H', 45)

F.left = B
F.right = G
B.left = A
B.right = D
D.left = C
D.right = E
G.right = I
I.left = H


def binary_tree_search(root, num):
    if root is None:
        return None

    if num < root.data:
        return binary_tree_search(root.left, num)
    elif num > root.data:
        return binary_tree_search(root.right, num)
    else:
        return root


def binary_tree_search_iterative(root, num):
    node = None
    while root is not None:
        if root.data == num:
            node = root
            break
        elif num < root.data:
            root = root.left
        elif num > root.data:
            root = root.right

    return node


def height(root):
    if root is None:
        return 0
    left_height = height(root.left)
    right_height = height(root.right)

    if left_height > right_height:
        return left_height + 1
    else:
        return right_height + 1


def inorder_predecessor(root):
    while root is not None and root.right is not None:
        root = root.right

    return root


def inorder_successor(root):
    while root is not None and root.left is not None:
        root = root.left

    return root


def binary_tree_insert(root, name, data):
    node = None
    if root is None:
        node = Node(name, data)
        return node

    if data < root.data:
        root.left = binary_tree_insert(root.left, name, data)
        # print(root)
    elif data > root.data:
        root.right = binary_tree_insert(root.right, name, data)
        # print(root)
    else:  # same value?
        root.name = name  # same node to be modified
        return root

    return root


def delete_binary_search_tree_node(root, key):

    if root is None:
        return None

    if root.left is None and root.right is None:
        if root.data == key:
            root = None
        return None

    if key < root.data:
        root.left = delete_binary_search_tree_node(root.left, key)
    elif key > root.data:
        root.right = delete_binary_search_tree_node(root.right, key)
    else:  # match found

        if height(root.left) > height(root.right):
            # find in-order predecessor
            node = inorder_predecessor(root.left)
            root.data = node.data  # assign the predecessor data to the node being deleted
            # delete the in_order predecessor node recursively. As we don't have access to the node directly,
            # we will traverse to the left of the found node with the original key
            root.left = delete_binary_search_tree_node(root.left, node.data)
        else:
            # find in-order predecessor
            node = inorder_successor(root.right)
            root.data = node.data  # assign the predecessor data to the node being deleted
            # delete the in_order successor node recursively. As we don't have access to the node directly,
            # we will traverse to the left of the found node with the original key
            root.right = delete_binary_search_tree_node(root.right, node.data)

    return root

# def delete_binary_search_tree_node(root, key):
#     if root is None:
#         return root

#     if key < root.data:
#         root.left = delete_binary_search_tree_node(root.left, key)
#     elif key > root.data:
#         root.right = delete_binary_search_tree_node(root.right, key)
#     else:
#         if root.left is None:
#             return root.right
#         elif root.right is None:
#             return root.left
#         else:
#             # Node with two children: find in-order successor
#             successor = inorder_successor(root.right)
#             root.data = successor.data
#             root.right = delete_binary_search_tree_node(
#                 root.right, successor.data)

#     return root


def in_order_traversal(root, result=None):

    if result is None:
        result = []

    if root == None:
        return

    in_order_traversal(root.left, result)
    result.append(root.data)
    in_order_traversal(root.right, result)

    return result


# A = Node('A', 15)
# D = Node('D', 25)
# I = Node('I', 50)
# C = Node('C', 10)
# E = Node('E', 27)
# H = Node('H', 45)

# print(binary_tree_search(F, 45))
# print(binary_tree_search_iterative(F, 45))
# root = binary_tree_insert(None, 'F', 30)
# binary_tree_insert(root, 'B', 20)
# binary_tree_insert(root, 'G', 40)
# # binary_tree_insert(root, 'G', 40)
# # binary_tree_insert(root, 'Z', 40)
# binary_tree_insert(root, 'A', 15)
# binary_tree_insert(root, 'D', 25)
# binary_tree_insert(root, 'I', 50)
# binary_tree_insert(root, 'C', 10)
# binary_tree_insert(root, 'E', 27)
# binary_tree_insert(root, 'H', 45)
# result = in_order_traversal(root)
# print(result)
# print(in_order_traversal(root))
# print(binary_tree_search(root, 20))
# delete_binary_search_tree_node(root, 30)
# print(in_order_traversal(root))
# delete_binary_search_tree_node(root, 20)
# print(in_order_traversal(root))
# delete_binary_search_tree_node(root, 40)
# print(in_order_traversal(root))

root = binary_tree_insert(None, 'F', 50)
binary_tree_insert(root, 'B', 10)
binary_tree_insert(root, 'G', 40)
binary_tree_insert(root, 'A', 20)
binary_tree_insert(root, 'D', 30)

print(in_order_traversal(root))

root = delete_binary_search_tree_node(root, 50)
print(in_order_traversal(root))
root = delete_binary_search_tree_node(root, 40)
print(in_order_traversal(root))
root = delete_binary_search_tree_node(root, 30)
print(in_order_traversal(root))
root = delete_binary_search_tree_node(root, 20)
print(in_order_traversal(root))
root = delete_binary_search_tree_node(root, 10)
print(in_order_traversal(root))
