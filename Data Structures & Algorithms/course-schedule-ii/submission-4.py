class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        dependents = { c:[] for c in range(numCourses) }
        indegree = [0] * numCourses

        for crs, pre in prerequisites:
            dependents[pre].append(crs)
            indegree[crs] += 1
        
        queue = deque(c for c in range(numCourses) if indegree[c] == 0)
        order = []

        while queue:
            crs = queue.popleft()
            order.append(crs)

            for dependent in dependents[crs]:
                indegree[dependent] -= 1

                if indegree[dependent] == 0:
                    queue.append(dependent)

        return order if len(order) == numCourses else []