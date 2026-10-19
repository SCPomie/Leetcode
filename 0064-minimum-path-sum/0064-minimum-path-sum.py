class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        # Extra row and column to handle boundaries
        # Infinity means we cannot take that direction
        dp = [[float("inf")] * (COLS + 1)
              for _ in range(ROWS + 1)]

        # Base case:
        # Allow the bottom-right cell to finish with no extra cost
        dp[ROWS - 1][COLS] = 0

        # Start at bottom-right and work towards top-left
        for r in range(ROWS - 1, -1, -1):
            for c in range(COLS - 1, -1, -1):

                # Minimum cost from this cell to destination
                # Choose between going DOWN or RIGHT
                dp[r][c] = grid[r][c] + min(
                    dp[r + 1][c],  # Cost if we go DOWN
                    dp[r][c + 1]   # Cost if we go RIGHT
                )

        # Minimum cost from start to destination
        return dp[0][0]