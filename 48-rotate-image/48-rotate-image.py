class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(matrix) - 1 # Start at first and last cols.
        while l < r:
            
            for i in range(r - l): # Last col handled in rotation.
                t, b = l, r
                # Save top left of curr rot.
                top_left = matrix[t][l + i]
                # Move bot-left to top-left.
                matrix[t][l + i] = matrix[b - i][l]
                # Move bot-right to bot-left.
                matrix[b - i][l] = matrix[b][r - i]
                # Move top-right to bot-right.
                matrix[b][r - i] = matrix[t + i][r]
                # Move top-left to top-right.
                matrix[t + i][r] = top_left
                
            # Move inwards to next level of rot.
            r -= 1
            l += 1
        