class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        #create the dp array. the +1 is needed because of the i + 1 index needed for the bottom row
        dp = [0] * (len(triangle) + 1)
        #iterate through the triangle list starting from the back
        for row in triangle[::-1]:
            #iterates through the values of each row
            for i, n in enumerate(row):
                #update the dp array with the current number + minimum of the previous dp value
                dp[i] = n + min(dp[i], dp[i + 1])
        #return dp[0] as that would be where the final answer locate
        return dp[0]