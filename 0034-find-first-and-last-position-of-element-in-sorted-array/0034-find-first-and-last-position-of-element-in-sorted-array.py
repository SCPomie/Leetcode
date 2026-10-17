class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Find the first and last occurrence of the target
        left = self.binarySearch(nums, target, True)
        right = self.binarySearch(nums, target, False)

        return [left, right]

    def binarySearch(self, nums, target, leftBias):
        # Initialise the left and right pointers and result index
        l, r = 0, len(nums) - 1
        i = -1

        # Binary search while the pointers haven't crossed
        while l <= r:
            m = (l + r) // 2

            # If target is greater, search right
            if target > nums[m]:
                l = m + 1

            # If target is smaller, search left
            elif target < nums[m]:
                r = m - 1

            else:
                # Save the index when target is found
                i = m

                # If finding the first occurrence, continue searching left
                if leftBias:
                    r = m - 1

                # Otherwise continue searching right for the last occurrence
                else:
                    l = m + 1

        return i
