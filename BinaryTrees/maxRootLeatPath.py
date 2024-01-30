class Binary:

    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


a = Binary(5)
b = Binary(11)
c = Binary(3)
d = Binary(4)
e = Binary(2)
f = Binary(1)

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


def max_root_leaf_path_sum(root):
    if not root:
        return 0
    left = max_root_leaf_path_sum(root.left)
    right = max_root_leaf_path_sum(root.right)
    return root.val + max(left, right)


print(max_root_leaf_path_sum(a))
