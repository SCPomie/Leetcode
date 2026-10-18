import heapq

class Solution:
    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
        # Edge case: return empty list if either array is empty
        if not nums1 or not nums2:
            return []

        res = []
        minHeap = []

        # Initialize heap with the first pair from each row
        # Store (sum, index in nums1, index in nums2)
        for i in range(min(k, len(nums1))):
            heapq.heappush(minHeap, (nums1[i] + nums2[0], i, 0))

        # Continue until we find k pairs or the heap is empty
        while minHeap and len(res) < k:
            # Pop the pair with the smallest sum
            total, i, j = heapq.heappop(minHeap)

            # Add the actual pair to the result
            res.append([nums1[i], nums2[j]])

            # Move to the next element in the same row (j + 1)
            if j + 1 < len(nums2):
                heapq.heappush(minHeap, (nums1[i] + nums2[j + 1], i, j + 1))

        return res