class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        premap = { i:[] for i in range(numCourses) }

        for crs, pre in prerequisites:
            premap[crs].append(pre)

        visiting = set()
        visited = set()
        res = []

        def dfs(crs):
            if crs in visiting:
                return False
            
            if crs in visited:
                return True
            
            visited.add(crs)
            visiting.add(crs)

            for pre in premap[crs]:
                if not dfs(pre):
                    return False
            
            res.append(crs)
            visiting.remove(crs)

            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return []
        
        return res
