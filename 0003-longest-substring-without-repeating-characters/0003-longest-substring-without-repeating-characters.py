class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0 
        strings = set()
        ans = 0
        #goes over the list
        for r in range(len(s)):
            # a while loop that checks for duplication
            while s[r] in strings:
                #removes the leftmost element until the duplicate element is removed 
                strings.remove(s[l])
                l += 1
            # adds the character into the list and calculate the current max length
            strings.add(s[r])
            ans = max(ans, len(strings))
        
        return ans