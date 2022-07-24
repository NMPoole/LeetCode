class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # Solution: O(m + n) time, O(1) additional space.
        
        n, m = len(matrix), len(matrix[0])
        row, col = n - 1, 0 # Start at bottom-left.
        
        while row >= 0 and col < m:
            
            if matrix[row][col] == target:
                return True
            
            if matrix[row][col] < target: # Eliminate curr col.
                col += 1
            else: # Eliminate curr col.
                row -= 1
                
        return False # Target does not exist.