class Solution:
    def longestPalindrome(self, s: str) -> str:
        resIdx, resLen = 0, 0
        n = len(s)

        # dp[i][j] = True if s[i:j+1] is a palindrome
        dp = [[False] * n for _ in range(n)]

        # Start from the end so inner substrings are checked first
        for i in range(n - 1, -1, -1):
            for j in range(i, n):

                # Outer characters must match
                # Length <= 3 is automatically valid if they match
                # Otherwise, check if the inner substring is a palindrome
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True

                    # Update the longest palindrome
                    if resLen < (j - i + 1):
                        resIdx = i
                        resLen = j - i + 1

        return s[resIdx : resIdx + resLen]