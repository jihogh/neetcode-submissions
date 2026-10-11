class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)

        # while we have 2 or more stones
        while len(heap) >= 2:
            first = heapq.heappop(heap)
            second = heapq.heappop(heap)

            if first < second:
                heapq.heappush(heap, first - second)
        
        return -heapq.heappop(heap) if heap else 0