class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []


        def backtrack(path):
            #base case
            if len(path) == len(nums):
                result.append(path.copy())
                return
            #loops through the inputs
            for num in nums:
                #if the number is already in the list then ignore it and continue to next cycle
                if num in path:
                    continue
                #append it to the path
                path.append(num)      
                #recursive call         
                backtrack(path)
                #removes the visit
                path.pop()  
                
        #calls the function and return the result
        backtrack([])
        return result