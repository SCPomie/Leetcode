import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-n for n in nums]
        heapq.heapify(nums)
        i = 1
        while i < k:
            heapq.heappop(nums)
            i += 1
        
        return -1 * heapq.heappop(nums)