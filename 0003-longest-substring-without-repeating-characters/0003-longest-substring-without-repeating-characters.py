class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0 
        strings = set()
        ans = 0

        for r in range(len(s)):
            while s[r] in strings:
                strings.remove(s[l])
                l += 1
            strings.add(s[r])
            ans = max(ans, len(strings))
        
        return ans