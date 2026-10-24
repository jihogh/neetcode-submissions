class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-w for w in stones]
        heapq.heapify(heap)

        # making the weights negative turns this into a max heap
        while len(heap) > 1:
            stone1 = heapq.heappop(heap)
            stone2 = heapq.heappop(heap)

            if stone1 != stone2:
                heapq.heappush(heap, stone1 - stone2)
        
        return -heap[0] if heap else 0