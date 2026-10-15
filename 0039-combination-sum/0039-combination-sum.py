class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        #result list
        result = []

        def backtrack(start, path, total):

            #base case if total equals target
            if total == target:
                result.append(path.copy())
                return

            #loop through the available candidates
            for i in range(start, len(candidates)):
                n = candidates[i]

                #skip if adding the number exceeds target
                if total + n > target:
                    continue

                #append the number
                path.append(n)

                #recursively call, allowing the same number to be reused
                backtrack(i, path, total + n)

                #undo the choice
                path.pop()

        #start backtracking
        backtrack(0, [], 0)
        return result