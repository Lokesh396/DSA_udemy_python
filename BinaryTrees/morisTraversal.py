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


def moris_traversal(root):
    curr = root
    while curr is not None:

        if curr.left is None:
            print(curr.val, end="->")
            curr = curr.right
        else:

            prev = curr.left
            while prev.right is not None and prev.right != curr:
                prev = prev.right

            if prev.right is None:
                prev.right = curr
                curr = curr.left

            else:
                prev.right = None
                print(curr.val, end="->")
                curr = curr.right


moris_traversal(a)
