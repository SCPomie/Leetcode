class Solution:
    def getMaxLen(self, nums: list[int]) -> int:
        #initialises all the variables needed
        result = 0
        l = 0
        neg = 0
        first_neg = -1
        #iterates through the input list
        for r in range(len(nums)):
            #if you encounter a 0, you have to reset everything because any product of 0 is 0
            if nums[r] == 0:
                l = r + 1
                neg = 0
                first_neg = -1
                continue
            #if you encounter a negative value
            if nums[r] < 0:
                #increment the count for negative value
                neg += 1
                #if it is the first negative value, record the r value
                if first_neg == -1:
                    first_neg = r
            #if the count of negative value is even, then you can calculate the leength by doing r - l
            if neg % 2 == 0:
                result = max(result, r - l + 1)
            else:
                #if it is an old number, the length would then be r - first_neg, which is the length without the first negative number which makes it even
                result = max(result, r - first_neg)
        #return the answer
        return result