class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        memo = {}

        def dfs(i):
            if i in memo:
                return memo[i]
                
            if amount - i in coins:
                return 1
            
            if i > amount:
                return -1

            # remember to propagate -1
            mincoins = float("inf")
            impossible = True
            for coin in coins:
                res = dfs(i+coin)
                if res != -1:
                    impossible = False
                    mincoins = min(mincoins, 1 + res)
            
            answer = mincoins if not impossible else -1
            memo[i] = answer
            return answer

        return dfs(0)