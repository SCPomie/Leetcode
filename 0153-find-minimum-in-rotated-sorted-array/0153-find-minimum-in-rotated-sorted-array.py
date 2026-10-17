class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Initialise the left and right pointers
        left, right = 0, len(nums) - 1

        # Binary search until both pointers meet
        while left < right:
            mid = (left + right) // 2

            # If mid is greater than right, minimum must be on the right
            if nums[mid] > nums[right]:
                left = mid + 1

            # Otherwise minimum is at mid or on the left
            else:
                right = mid

        # Return the minimum element
        return nums[left]