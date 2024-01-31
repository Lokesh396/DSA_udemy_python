class Binary:

    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


a = Binary(11)
b = Binary(5)
c = Binary(14)
d = Binary(4)
e = Binary(6)
f = Binary(15)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      a
#     / \
#    b    c
#  /  \    \
# d    e    f


# A valid BST is defined as follows:
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.


def valid_binary_tree(root, min_value, max_value):
    if not root:
        return True
    if not min_value < root.val < max_value:
        return False
    return valid_binary_tree(root.left, min_value, root.val) and valid_binary_tree(root.right, root.val, max_value)


print(valid_binary_tree(a, -float('inf'), float('inf')))
