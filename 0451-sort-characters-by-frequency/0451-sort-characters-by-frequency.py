class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        pairs = sorted(freq.items(), key = lambda x: x[1], reverse = True)
        return "".join(ch * cnt for ch, cnt in pairs)