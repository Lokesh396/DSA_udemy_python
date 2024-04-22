"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
"""

#            1
#          /    \
#         2      2
#        / \    / \
#       3   4  4   3


# solution 1

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def mirror(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            
            return mirror(left.left, right.right) and mirror(left.right, right.left)
        
        if not root:
            return True
        
        return mirror(root.left, root.right)


# solution 2

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution2:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        res1 = []
        res2 = []

        def inorder1(root, f):
            if root:
                inorder1(root.left, 'l')
                res1.append(str(root.val) + f)
                inorder1(root.right, 'r')
        inorder1(root.left, 'l')
        def inorder2(root, f):
            if root:
                inorder2(root.right, 'l')
                res2.append(str(root.val) + f)
                inorder2(root.left, 'r')
        inorder2(root.right, 'l')
        return res1 == res2