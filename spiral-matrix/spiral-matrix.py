class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # Solution: O(m n) time, O(1) additional space.
        
        if not matrix or not matrix[0]:
            return []
        
        start_row, end_row, start_col, end_col = 0, len(matrix), 0, len(matrix[0])
        output = []
        
        while start_row < end_row and start_col < end_col:
            
            if start_row < end_col: # Right.
                output.extend([matrix[start_row][i] for i in range(start_col, end_col)])
            start_row += 1
            
            if start_col < end_col: # Down.
                output.extend([matrix[i][end_col - 1] for i in range(start_row, end_row)])
            end_col -= 1
            
            if start_row < end_row: # Left.
                output.extend([matrix[end_row - 1][i] for i in range(end_col - 1, start_col - 1, -1)])
            end_row -= 1
            
            if start_col < end_col: # Up.
                output.extend([matrix[i][start_col] for i in range(end_row - 1, start_row - 1, -1)])
            start_col += 1
            
        return output