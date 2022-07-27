# //! Naive Solution

# Link: https://leetcode.com/problems/valid-sudoku/

# Time Complexity: O(n^2)
# Space Complexity: O(n^2)


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows
        for row in board:
            nums = [int(ch) for ch in row if ch != '.']
            if len(nums) != len(set(nums)):
                return False

        # Check columns
        columns = list(zip(*board))
        for col in columns:
            nums = [int(ch) for ch in col if ch != '.']
            if len(nums) != len(set(nums)):
                return False

        # Check 3x3 sub-boxes
        for i in range(0, len(board), 3):
            for j in range(0, len(board), 3):
                submatrix = [board[x][y] for y in range(j, j + 3)
                                         for x in range(i, i + 3)
                                         if board[x][y] != '.']
                if len(submatrix) != len(set(submatrix)):
                    return False

        return True
