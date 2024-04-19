"""
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        m = root.val
        c = [0]
        def dfs(root,  m):
            if root:
                if root.val >= m:
                    c[0] += 1
                dfs(root.left, max(m, root.val))
                dfs(root.right, max(m, root.val))

        dfs(root, m)
        return c[0]
            
