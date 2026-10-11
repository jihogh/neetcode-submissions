class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = { i:[] for i in range(n) }
        visited = set()
        components = 0

        for node1, node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)
        
        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)

            for neighbor in adj[node]:
                dfs(neighbor)
        
        for i in range(n):
            if i not in visited:
                dfs(i)
                components += 1
        
        return components