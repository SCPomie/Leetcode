class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count_map = {}
        res = 0

        l = 0
        most_freq = 0
        for r in range(len(s)):
            count_map[s[r]] = 1 + count_map.get(s[r], 0)
            most_freq = max(most_freq, count_map[s[r]])

            while (r - l + 1) - most_freq > k:
                count_map[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        return res        