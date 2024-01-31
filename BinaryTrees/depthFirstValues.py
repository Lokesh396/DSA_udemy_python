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

# Iterative Approach
# def depth_first(root):
#     if not root:
#         return []
#     result = []
#     stack = [root]
#     while len(stack):
#         current = stack.pop()
#         result.append(current.val)
#         if current.right:
#             stack.append(current.right)
#         if current.left:
#             stack.append(current.left)
#     return result


# Recursive Approach
def depth_first(root):
    if not root:
        return []
    left_values = depth_first(root.left)
    right_values = depth_first(root.right)
    values = [root.val]
    values.extend(left_values)
    values.extend(right_values)
    return values


print(depth_first(a))
