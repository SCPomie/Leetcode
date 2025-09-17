class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        count_t = {}
        for c in t:
            count_t[c] = count_t.get(c,0) + 1
        required = len(count_t)
        best_window = float("inf")
        best_start = 0
        formed = 0

        count_s = {}
        l = 0
        for i, r in enumerate(s):
            count_s[r] = count_s.get(r, 0) + 1

            if r in count_t and count_t[r] == count_s[r]:
                formed += 1
            
            while formed == required:
                curr_window = i - l + 1

                if curr_window < best_window:
                    best_window = curr_window
                    best_start = l

                left_char = s[l]
                count_s[left_char] -= 1

                if left_char in count_t and count_s[left_char] < count_t[left_char]:
                    formed -= 1

                l += 1
        return "" if best_window == float("inf") else s[best_start: best_start + best_window]

