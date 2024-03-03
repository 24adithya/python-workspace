class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


F = Node('F')  # root
B = Node('B')
G = Node('G')
A = Node('A')
D = Node('D')
I = Node('I')
C = Node('C')
E = Node('E')
H = Node('H')

F.left = B
F.right = G
B.left = A
B.right = D
D.left = C
D.right = E
G.right = I
I.left = H

#             F
#           /   \
#          B      G
#         / \     /\
#        A   D    n I
#       /\  / \    / \
#      n n  C  E   H  n
#          /\  /\  /\
#          n n n n n

#  preorder - FBADCEGIH;
#  inorder - ABCDEFGHI;
#  postorder - ACEDBHIGF;


def pre_order_traversal(root, result=[]):
    if root == None:
        return

    result.append(root.val)
    pre_order_traversal(root.left)
    pre_order_traversal(root.right)

    return result


def in_order_traversal(root, result=[]):
    if root == None:
        return

    in_order_traversal(root.left)
    result.append(root.val)
    in_order_traversal(root.right)

    return result


def post_order_traversal(root, result=[]):
    if root == None:
        return

    post_order_traversal(root.left)
    post_order_traversal(root.right)
    result.append(root.val)

    return result


def count_leaf_nodes(root):
    if root == None:
        return 0

    left_child = count_leaf_nodes(root.left)
    right_child = count_leaf_nodes(root.right)

    if root.left == None and root.right == None:
        return left_child + right_child + 1

    return left_child + right_child


def get_leaf_nodes(root, res=[]):  # also knows as external nodes or nodes with decree '0'
    if root == None:
        return

    get_leaf_nodes(root.left, res)
    get_leaf_nodes(root.right, res)

    if root.left == None and root.right == None:
        res.append(root.val)
        return res

    return res


# also knows as internal nodes or nodes with decree > '0'
def get_internal_nodes(root, res=[]):
    if root == None:
        return

    get_internal_nodes(root.left, res)
    get_internal_nodes(root.right, res)

    if root.left != None or root.right != None:
        res.append(root.val)
        return res

    return res


def get_nodes_with_decree_1(root, res=[]):
    if root == None:
        return

    get_nodes_with_decree_1(root.left, res)
    get_nodes_with_decree_1(root.right, res)

    if root.left == None and root.right != None or root.left != None and root.right == None:
        res.append(root.val)
        return res

    return res


def count_nodes(root, res=[]):
    if root == None:
        return 0

    return count_nodes(root.left, res) + count_nodes(root.right, res) + 1


def get_tree_height(root):
    if root == None:
        return -1

    left_tree_height = get_tree_height(root.left)
    right_tree_height = get_tree_height(root.right)

    if left_tree_height < right_tree_height:
        return right_tree_height + 1
    else:
        return left_tree_height + 1


print(pre_order_traversal(F))
print(in_order_traversal(F))
print(post_order_traversal(F))

print(count_leaf_nodes(F))
print(get_leaf_nodes(F))
print(get_internal_nodes(F))
print(get_nodes_with_decree_1(F))
print(f'Total nodes : {count_nodes(F)}')
print(f'Height of binary tree : {get_tree_height(F)}')
