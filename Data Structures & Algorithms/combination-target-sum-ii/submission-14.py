class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        cur = []

        def dfs(index, total):
            if total > target:
                return
            elif total == target:
                res.append(cur.copy())
                return
            
            if index == len(candidates):
                return
            
            # take and repeat index
            cur.append(candidates[index])
            dfs(index+1, total + candidates[index])

            # skip and skip all dupes
            cur.pop()
            while index < len(candidates) - 1 and candidates[index+1] == candidates[index]:
                index += 1
            
            dfs(index+1, total)

        dfs(0, 0)
        return res