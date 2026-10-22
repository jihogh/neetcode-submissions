class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for i in range(n)]

        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = set()
        res = 0

        def dfs(node):
            nonlocal res
            if node in visited:
                return
            else:
                visited.add(node)

            for nei in adj[node]:
                dfs(nei)
            return
        
        for c in range(n):
            if c not in visited:
                dfs(c)
                res += 1
        
        return res