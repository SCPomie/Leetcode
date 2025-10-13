class Solution:
    def frequencySort(self, s: str) -> str:
        ans = {}
        
        for ch in s:
            if ch not in ans:
                ans[ch] = 0
            ans[ch] += 1
        res = []
        for key, value in ans.items():
            res.append((key, value))
        
        result = sorted(res, key = lambda x:x[1], reverse = True)
        str_res = ""
        for n in result:
            str_res += n[0] * n[1]
        return str_res