class Binary:

    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


a = Binary(3)
b = Binary(11)
c = Binary(4)
d = Binary(4)
e = Binary(6)
f = Binary(4)

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


def tree_min_value(root):
    if not root:
        return float('inf')
    left = tree_min_value(root.left)
    right = tree_min_value(root.right)
    return min(root.val, left, right)


print(tree_min_value(root=a))