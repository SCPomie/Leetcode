class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #set up the left and right to count the index
        left = 0
        right = len(nums) - 1
        #a while loop which iterates through the array and cutting it down by half each time
        while left <= right:
            mid = (left + right) // 2
            #if the mid value is equal to the target then return mid
            if nums[mid] == target:
                return mid
            #if mid value is smaller than the target then left is added by the mid vlaue making left equal to mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                #changes right to mid, similar to the above statement
                right = mid - 1
        #returns left which would be the posiiton of the target
        return left
        
        