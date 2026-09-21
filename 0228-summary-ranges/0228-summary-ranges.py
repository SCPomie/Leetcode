class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        #initialise the ans list
        ans = []

        i = 0
        #while loop starting from the start
        while i < len(nums):
            start = nums[i]
            # another while loop, increments the i and stops when there is a gap between the numbers
            while i < len(nums) - 1 and nums[i] + 1 == nums[i + 1]:
                i += 1
            #adds the intervals to the answert else just add the ith number
            if start != nums[i]:
                ans.append(str(start) + "->" + str(nums[i]))
            else:
                ans.append(str(nums[i]))
            #increment i so that the new loop start on the next value
            i += 1
        #returns the answer
        return ans