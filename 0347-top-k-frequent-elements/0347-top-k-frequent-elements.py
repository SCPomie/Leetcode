class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for n in nums:
            counts[n] = counts.get(n, 0) + 1
        counts = sorted(counts.items(), key=lambda x:x[1], reverse=True)
        ans = []
        for i in range(k):
            ans.append(counts[i][0])
        return ans
        