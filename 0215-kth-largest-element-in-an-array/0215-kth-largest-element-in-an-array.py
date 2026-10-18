import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #convert the list into negatives as python heapq is minium at the top
        nums = [-n for n in nums]
        #convert the nums to a heap
        heapq.heapify(nums)
        i = 1
        #iterate through the heap and pop the largest number until k - 1
        while i < k:
            heapq.heappop(nums)
            i += 1
        #pop the kth largest number, * -1 to make it positive
        return -1 * heapq.heappop(nums)