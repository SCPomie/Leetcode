class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        total = 0
        while l != r and l < r:
            if (height[l] >= height[r]):
                amount = (r - l) * height[r]
            else:
                amount = (r - l) * height[l]
            if (amount >= total):
                total = amount
            
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return total