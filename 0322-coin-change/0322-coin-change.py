class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        #define the dp
        dp = [float("inf")] * (amount + 1)
        #base case, coin's needed for 0 is 0
        dp[0] = 0
        
        #loops through 1-amount - 1, to get the previous dp array values
        for a in range(1, amount + 1):
            #iterates through the coins
            for coin in coins:
                #if amount - chosen coin >= 0, only use the coin that doesn't exceed the amount
                if a - coin >= 0:
                    #gets the dp value[a] = minimum of the original dp[a] value or 1 + dp[a - coin]
                    dp[a] = min(dp[a], 1 + dp[a - coin])
        #return the result
        return dp[amount] if dp[amount] != float("inf") else -1