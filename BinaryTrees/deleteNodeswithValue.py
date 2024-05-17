
# Delete leaves with a given value

"""
Given a binary tree root and an integer target, delete all the leaf nodes with value target.

Note that once you delete a leaf node with value target, if its parent node becomes a leaf node and has the value
target, it should also be deleted (you need to continue doing that until you cannot).
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def removeLeafNodes(self, root, target: int):

        # def checkNode(root):
        #      if root:
        #         if not root.left and not root.right:
        #             if root.val == target:
        #                 return None
        #             return root
        #         return root

        def constructTree(root):
            if root:
                root.left = constructTree(root.left)
                root.right = constructTree(root.right)
                if not root.left and not root.right:
                    if root.val == target:
                        return None
                return root

        return constructTree(root)
