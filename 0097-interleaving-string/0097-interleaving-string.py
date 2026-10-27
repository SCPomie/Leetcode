class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        #base case if they are not equal then return False
        if len(s1) + len(s2) != len(s3):
            return False

        #create the dp
        dp = [[False] * (len(s2) + 1) for i in range(len(s1) + 1)]
        dp[len(s1)][len(s2)] = True

        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                #Can I take the next character from s1 and still finish the string? Look at dp[i+1][j]
                if i < len(s1) and s1[i] == s3[i + j] and dp[i + 1][j]:
                    dp[i][j] = True
                #Can I take the next character from s2 and still finish the string? Look at dp[i][j+1].
                if j < len(s2) and s2[j] == s3[i + j] and dp[i][j + 1]:
                    dp[i][j] = True
        return dp[0][0]
        