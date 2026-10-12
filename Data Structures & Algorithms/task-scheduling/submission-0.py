class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        
        # we need to do -c becase heapq is minHeap in python
        maxHeap = [-c for c in count.values()]

        heapq.heapify(maxHeap)

        time = 0
        q = deque() # pairs of [-cnt, idleTime] at what time is it available

        while maxHeap or q:
            time += 1

            if maxHeap:
                # add one because we're using neg values
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time+n])
            
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        
        return time