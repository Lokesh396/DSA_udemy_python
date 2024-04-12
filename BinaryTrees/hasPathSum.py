"""
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def pathSum(root, target, curr_sum):
            if root:
                if not root.left and not root.right:
                    if curr_sum + root.val == target:
                        return True
                l = pathSum(root.left, target, curr_sum + root.val)
                r = pathSum(root.right, target, curr_sum + root.val)
                return l or r
        return pathSum(root, targetSum , 0)
        