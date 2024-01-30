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


def depth_first_values(root):
    if not root:
        return []
    queue = [root]
    result = []
    while len(queue):
        current = queue.pop(0)
        result.append(current.val)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return result


print(depth_first_values(root=a))
