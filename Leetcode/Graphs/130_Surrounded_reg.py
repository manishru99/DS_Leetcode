# 130. Surrounded Regions

# Logic: Capture surrounded regions (original problem)
# Do reverse engg & logic change to:
# Capture everything except unsorrounded regions

'''- Border-connected 'O's are safe → marked as 'T'
- Interior 'O's are surrounded → flipped to 'X'
- Final pass → restore 'T' back to 'O'
'''
# Time complexity: O(m * n)
# Space complexity: O(m * n)

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # Get the dimensions of the board
        ROWS, COLS = len(board), len(board[0])

        # DFS function to mark all 'O's connected to the border
        def capture(r, c): # change method name to dfs
            # If out of bounds or not an 'O', return
            if (r < 0 or c < 0 or r == ROWS or
                c == COLS or board[r][c] != "O"
            ):
                return
            # Temporarily mark the cell to indicate it's safe (connected to border)
            board[r][c] = "T"
            # Recursively visit all 4 directions
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)

        # Step 1: Mark all 'O's connected to the border as safe
        for r in range(ROWS):
            # 1st col
            if board[r][0] == "O":
                capture(r, 0)
            # last col
            if board[r][COLS - 1] == "O":
                capture(r, COLS - 1)

        for c in range(COLS):
            # 1st row
            if board[0][c] == "O":
                capture(0, c)
            # last row
            if board[ROWS - 1][c] == "O":
                capture(ROWS - 1, c)

        # Step 2: Flip all remaining 'O's to 'X' (they are surrounded)
        # and revert 'T' back to 'O' (they were connected to border)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"