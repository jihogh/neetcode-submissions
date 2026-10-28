class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = { i:[] for i in range(numCourses) }

        for pre, crs in prerequisites:
            preMap[crs].append(pre)

        visiting = set()

        def dfs(node):
            if node in visiting:
                return False
            
            if preMap[node] == []:
                return True
            
            visiting.add(node)

            for nei in preMap[node]:
                if not dfs(nei):
                    return False
            
            visiting.remove(node)

            preMap[node] = []

            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False

        return True