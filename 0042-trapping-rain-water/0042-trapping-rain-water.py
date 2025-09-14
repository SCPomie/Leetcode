class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxLeft, maxRight = 0, 0
        water = 0

        while l < r:
            if height[l] < height[r]:
                if height[l] >= maxLeft:
                    maxLeft = height[l]
                else:
                    water += maxLeft - height[l]
                l += 1
            else:
                if height[r] >= maxRight:
                    maxRight = height[r]
                else:
                    water += maxRight - height[r]
                r -= 1
        
        return water