# 51. N-Queens

class Solution:
    def isSafe1(self, row, col, board, n):
        # check left upper diagonal
        duprow = row
        dupcol = col

        while row >= 0 and col >= 0:
            if board[row][col] == 'Q':
                return False
            row -= 1
            col -= 1

        # check straight left side
        col = dupcol
        row = duprow
        while col >= 0:
            if board[row][col] == 'Q':
                return False
            col -= 1

        # check left lower diagonal
        row = duprow
        col = dupcol
        while row < n and col >= 0:
            if board[row][col] == 'Q':
                return False
            row += 1
            col -= 1

        return True


    def solve(self, col, board, ans, n):
        # base
        if col == n:
            ans.append(list(board))
            return


        for row in range(n):
            if self.isSafe1(row, col, board, n):
                #board[row] = board[row][:col] + 'Q' + board[row][col+1:]
                # Convert row string to a list to mutate it
                temp = list(board[row])
                temp[col] = 'Q'
                board[row] = ''.join(temp)

                # solve for next col recursively
                self.solve(col+1, board, ans, n)
                #board[row] = board[row][:col] + '.' + board[row][col+1:]
                # Backtrack: reset to '.'
                temp[col] = '.'
                board[row] = ''.join(temp)


    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        board = ['.'*n for _ in range(n)]
        self.solve(0, board, ans, n)
        return ans
'''
Time Complexity: O(N!)
- For each column, you attempt to place a queen in N rows.
- At each level of recursion, you go to the next column and try all safe rows.
- Due to the pruning with isSafe1, not all Nⁿ combinations are explored, but in the worst case, the number of valid configurations can approach N!
- So, the upper bound is O(N!), which matches the number of permutations of queens in different rows and columns.

🧠 Space Complexity: O(N²) (or O(N) if you optimize the board)
- The board is a list of N strings, each of length N → O(N²) space
- The recursion depth is N, so the call stack space is O(N)
- If you represented the board more compactly (like with a list of integers for queen positions per column), you could reduce space to O(N).
'''

# Optimized

class Solution:
    def solve(self, col, board, ans, leftrow, upperDiagonal, lowerDiagonal, n):
        if col == n:
            ans.append(board[:])
            return


        for row in range(n):
            if leftrow[row] == 0 and lowerDiagonal[row+col] == 0 and upperDiagonal[n-1+col-row] == 0:
                board[row] = board[row][:col] + 'Q' + board[row][col+1:]
                leftrow[row] = 1
                lowerDiagonal[row+col] = 1
                upperDiagonal[n-1+col-row] = 1
                self.solve(col+1, board, ans, leftrow,
                           upperDiagonal, lowerDiagonal, n)
                board[row] = board[row][:col] + '.' + board[row][col+1:]
                leftrow[row] = 0
                lowerDiagonal[row+col] = 0
                upperDiagonal[n-1+col-row] = 0


    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        board = ['.'*n for _ in range(n)]
        leftrow = [0]*n
        upperDiagonal = [0]*(2*n-1)
        lowerDiagonal = [0]*(2*n-1)
        self.solve(0, board, ans, leftrow, upperDiagonal, lowerDiagonal, n)
        return ans

