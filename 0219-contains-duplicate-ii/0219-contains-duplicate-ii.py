class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        #initialise the dictionary
        score = {}
        #loops over the list
        for i in range(len(nums)):
            #if the current value is inside the dictionary, compared it with the last appearance of it
            # in the dictionary. 
            if nums[i] in score and abs(i - score[nums[i]]) <= k:
                return True
            # adds only the most recent index of the value into the dictionary
            score[nums[i]] = i
        
        return False
    