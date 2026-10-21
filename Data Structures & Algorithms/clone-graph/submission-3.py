"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            
            new = Node(node.val)

            oldToNew[node] = new

            for old in node.neighbors:
                new.neighbors.append(dfs(old))

            return new
        
        return dfs(node) if node else None