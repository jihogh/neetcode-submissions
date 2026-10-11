class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            largest = 0
            second = 0
            for stone in stones:
                if stone > largest:
                    second = largest
                    largest = stone
                elif stone > second:
                    second = stone

            print(stones)
            print(largest, second)
            
            stones.remove(largest)
            stones.remove(second)

            if largest != second:
                stones.append(largest-second)
        
        return stones[0] if stones else 0