"""
A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.

Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node of the tree as the root. When you select a node x as the root, the result tree has height h. Among all possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).

Return a list of all MHTs' root labels. You can return the answer in any order.

The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.


"""

# Initial Intution 

class Solution1:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges:
            return [0]
        tree = {}
        def buildTree(edges):
            for node1, node2 in edges:
                if node1 not in tree:
                    tree[node1] = []
                if node2 not in tree:
                    tree[node2] = []
                tree[node1].append(node2)
                tree[node2].append(node1)
        
        buildTree(edges)

        visited = set()
        def height(root):
            stack = [(root, 0)]
            max_height = 0
            while stack:
                curr, h = stack.pop()
                max_height = max(max_height, h)
                visited.add(curr)
                for child in tree[curr]:
                    if child not in visited:
                        stack.append((child, h + 1))
            return max_height
        

        min_height = float('inf')
        result = []
        for key in tree.keys():
            h = height(key)
            if h < min_height:
                result = [key]
                min_height = h
            elif h == min_height:
                result.append(key)
            visited.clear()
        return result


# optimized solution

# The intution is at most ther will be 2 minimum height trees 

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges:
            return [0]
        tree = {}
 
        def buildTree(edges):
            for node1, node2 in edges:
                if node1 not in tree:
                    tree[node1] = []
                if node2 not in tree:
                    tree[node2] = []
                tree[node1].append(node2)
                tree[node2].append(node1)
        
        buildTree(edges)
        leaves = [node for node in tree if len(tree[node]) == 1]

        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                neighbor = tree[leaf].pop()
                tree[neighbor].remove(leaf)
                if len(tree[neighbor]) == 1:
                    new_leaves.append(neighbor)
            leaves = new_leaves
        
        return leaves