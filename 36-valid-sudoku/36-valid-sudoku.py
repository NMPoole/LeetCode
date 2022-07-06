class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = defaultdict(set) # Each row gets a set of values in the row.
        cols = defaultdict(set) # Each column gets a set of values in the col.
        squares = defaultdict(set) # Each square gets a set of values in the square: key=(r//3,c//3).
        
        # Iterate over every square inside the grid.
        for r in range(9):
            for c in range(9):
                
                if board[r][c] == ".": # Skip over blank cells.
                    continue
                
                # If curr value already in current row, column, or square, then duplicate so invalid.
                if (board[r][c] in rows[r] or 
                    board[r][c] in cols[c] or 
                    board[r][c] in squares[(r // 3, c // 3)]):
                        return False
                
                # Continue, but update structures with current square value.
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
                
        return True
                    