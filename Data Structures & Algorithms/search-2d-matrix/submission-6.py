class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = 0, len(matrix) - 1

        while left <= right:
            row = (left + right) // 2

            if target > matrix[row][-1]:
                left = row + 1
            elif target < matrix[row][0]:
                right = row - 1
            else:
                break

        if not (left <= right):
            return False

        left, right = 0, len(matrix[row])

        while left <= right:
            mid = (left + right) // 2

            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                left += 1
            else:
                right -= 1
        
        return False