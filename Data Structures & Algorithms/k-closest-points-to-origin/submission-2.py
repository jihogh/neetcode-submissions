class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []

        for x,y in points:
            if len(maxHeap) < k:
                heapq.heappush(maxHeap, (-(x*x + y*y),x,y))
            else:
                if -(maxHeap[0][0]) > (x*x + y*y):
                    heapq.heappop(maxHeap)
                    heapq.heappush(maxHeap, (-(x*x + y*y),x,y))
        
        return [[x,y] for (d,x,y) in maxHeap]