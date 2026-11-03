
class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        ROWS, COLS = len(coins), len(coins[0])

        # Store maximum profit for each cell and k
        dp = [[[float("-inf")] * 3 for _ in range(COLS)] for _ in range(ROWS)]

        # Traverse from bottom-right to top-left
        for r in range(ROWS - 1, -1, -1):
            for c in range(COLS - 1, -1, -1):
                value = coins[r][c]

                for k in range(3):
                    # Handle destination
                    if r == ROWS - 1 and c == COLS - 1:
                        dp[r][c][k] = max(value, 0) if k > 0 else value
                        continue

                    # Find best path moving down or right
                    down = dp[r + 1][c][k] if r + 1 < ROWS else float("-inf")
                    right = dp[r][c + 1][k] if c + 1 < COLS else float("-inf")

                    # Take current cell value
                    result = value + max(down, right)

                    # Try neutralizing the robber
                    if value < 0 and k > 0:
                        down_neutral = dp[r + 1][c][k - 1] if r + 1 < ROWS else float("-inf")
                        right_neutral = dp[r][c + 1][k - 1] if c + 1 < COLS else float("-inf")

                        result = max(result, down_neutral, right_neutral)

                    # Store maximum profit
                    dp[r][c][k] = result

        return dp[0][0][2]



    #start at (0, 0) with 2 neturalisation
        return dfs(0, 0, 2)

