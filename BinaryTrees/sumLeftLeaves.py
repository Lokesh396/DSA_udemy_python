"""
Given the root of a binary tree, return the sum of all left leaves.

A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        total = [0]
        def leftSum(root):
            if root:
                if not root.left and not root.right:
                    return root.val
                l = leftSum(root.left)
                r = leftSum(root.right)
                total[0] += l or 0
        
        leftSum(root)
        return total[0]