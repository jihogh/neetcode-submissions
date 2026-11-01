class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # tree if acyclical
        adj = { i:[] for i in range(n) }

        for node1, node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)

        visiting = set()

        def dfs(node, par):
            if node in visiting:
                return False
            
            visiting.add(node)

            for nei in adj[node]:
                if nei == par:
                    continue
                elif not dfs(nei, node):
                    return False
            
            return True
        
        return dfs(0,-1) and len(visiting) == n