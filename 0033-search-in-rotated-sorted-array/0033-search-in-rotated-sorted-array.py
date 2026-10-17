class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Initialise the left and right pointers
        l, r = 0, len(nums) - 1

        # Binary search through the array
        while l <= r:
            mid = (l + r) // 2

            # Return mid if the target is found
            if target == nums[mid]:
                return mid

            # Check if the left half is sorted
            if nums[l] <= nums[mid]:

                # If target is outside the sorted left half, search right
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1

                # Otherwise search the left half
                else:
                    r = mid - 1

            # Otherwise the right half is sorted
            else:

                # If target is outside the sorted right half, search left
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1

                # Otherwise search the right half
                else:
                    l = mid + 1

        # Return -1 if the target is not found
        return -1