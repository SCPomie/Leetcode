
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()

        if len(pattern) != len(s):
            return False

        patterns = {}
        words = {}

        for i in range(len(s)):
            if ((pattern[i] in patterns and patterns[pattern[i]] != s[i]) or
                (s[i] in words and words[s[i]] != pattern[i])):
                return False

            patterns[pattern[i]] = s[i]
            words[s[i]] = pattern[i]

        return True