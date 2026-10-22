class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        premap = { i:[] for i in range(numCourses) }

        for crs, pre in prerequisites:
            premap[crs].append(pre)

        output = []
        visited, visiting = set(), set()

        def dfs(crs):
            if crs in visiting:
                # cycle detected
                return False

            if crs in visited:
                return True
            
            visiting.add(crs)

            for pre in premap[crs]:
                if dfs(pre) == False:
                    return False

            visiting.remove(crs)
            visited.add(crs)
            output.append(crs)
            return True
        
        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return output