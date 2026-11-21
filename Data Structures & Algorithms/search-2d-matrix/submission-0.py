class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        l, r = 0, m * n - 1

        while l <= r:
            m = (l + r) // 2
            row, col = m // n, m % n

            if matrix[row][col] == target:
                return True
            
            if matrix[row][col] < target:
                l = m + 1
            else:
                r = m - 1
        
        return False


        