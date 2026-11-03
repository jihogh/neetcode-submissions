class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowDict = defaultdict(set)
        colDict = defaultdict(set)
        boxDict = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[0])):
                cur = board[r][c]

                if cur in rowDict[r] or cur in colDict[c] or cur in boxDict[(r // 3,c // 3)]:
                    if cur != ".":
                        return False

                rowDict[r].add(cur)
                colDict[c].add(cur)
                boxDict[(r // 3,c // 3)].add(cur)


        return True