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
