class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        left = 0
        right = m - 1

        while left <= right:
            mid_n = (left + right) // 2

            if matrix[mid_n][0] <= target <= matrix[mid_n][n - 1]:
                left = 0
                right = n - 1
                break
            elif matrix[mid_n][-1] < target:
                left = mid_n + 1
            else:
                right = mid_n - 1

        while left <= right:
            mid_m = (left + right) // 2

            if matrix[mid_n][mid_m] == target:
                return True
            elif matrix[mid_n][mid_m] < target:
                left = mid_m + 1
            else:
                right = mid_m - 1

        return False