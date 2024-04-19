"""
Given the root of a binary search tree, and an integer k, return the kth Largest value (1-indexed) of all the values of the nodes in the tree.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargest(self, root: Optional[TreeNode], k: int) -> int:

        n = 0
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.right
            curr = stack.pop()
            n += 1
            if n == k:
                return curr.val
            curr = curr.left