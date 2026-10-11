class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            first = heapq.heappop(heap)
            second = heapq.heappop(heap)

            if second > first:
                heapq.heappush(heap, first-second)
        
        heap.append(0)
        return abs(heap[0])