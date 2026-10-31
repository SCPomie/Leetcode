class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        #the number of operations is the numnber of distinct values in the given list
        sets = set()

        for num in nums:
            if num != 0:
                sets.add(num)
        
        return len(sets)