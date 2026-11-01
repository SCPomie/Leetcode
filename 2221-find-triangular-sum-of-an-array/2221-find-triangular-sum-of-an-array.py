class Solution:
    def triangularSum(self, nums: list[int]) -> int:
        #base case when nums only has 1 digit
        if len(nums) == 1:
            return nums[0]
        #gets the old array
        old_array = nums
        #loop through the list starting from 1
        for i in range(1, len(nums)):
            #create a new list every time but decrease the size by i
            new_array = [0] * (len(nums) - i)
            #loop through the new list
            for j in range(len(new_array)):
                #start the calculation for the new list
                new_array[j] = (old_array[j] + old_array[j + 1]) % 10
            #make the old array to be the new array
            old_array = new_array
        #return the number at index 0
        return new_array[0]
