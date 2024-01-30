class Binary:

    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


a = Binary('a')
b = Binary('b')
c = Binary('c')
d = Binary('d')
e = Binary('e')
f = Binary('f')

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


# def tree_includes(root, value):
#     if not root:
#         return False
#     queue = [root]
#     while queue:
#         current = queue.pop(0)
#         if current.val == value:
#             return True
#         if current.left:
#             queue.append(current.left)
#         if current.right:
#             queue.append(current.right)
#     return False


def tree_includes(root, value):
    if not root:
        return False
    if root.val == value:
        return True
    left = tree_includes(root.left, value)
    right = tree_includes(root.right, value)
    return left or right


print(tree_includes(root=a, value='e'))
