class Binary:

    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


a = Binary(3)
b = Binary(11)
c = Binary(4)
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


# def tree_sum(root):
#     if not root:
#         return 0
#     left = tree_sum(root.left)
#     right = tree_sum(root.right)
#     return left + root.val + right

def tree_sum(root):
    if not root:
        return 0
    queue = [root]
    total = 0
    while queue:
        current = queue.pop(0)
        total += current.val
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return total


print(tree_sum(root=a))
