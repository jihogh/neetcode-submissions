class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        
        two = 1
        one = 1

        for step in range(2, n+1):
            tmp = one
            one = one + two
            two = tmp
        
        return one