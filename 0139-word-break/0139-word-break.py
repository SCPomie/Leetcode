class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp[i] = True if the substring s[i:] can be segmented into words
        dp = [False] * (len(s) + 1)

        # Base case: Empty string can be segmented successfully
        dp[len(s)] = True

        # Work backwards from the end of the string
        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                # Check if the word fits and matches the substring
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    # Check if the remaining substring can also be segmented
                    dp[i] = dp[i + len(w)]

                # Stop checking once we find a valid segmentation
                if dp[i]:
                    break

        # True if the entire string can be segmented
        return dp[0]