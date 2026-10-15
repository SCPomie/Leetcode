class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        #result list
        result = []

        def backtrack(start, path):
            #base case to return
            if len(path) == k:
                result.append(path.copy())
                return
            
            for num in range(start, n + 1):

                #choose a number
                path.append(num)

                #recursively choose the next number
                backtrack(num + 1, path)

                #undo the choice
                path.pop()
        
        backtrack(1, [])
        return result
        