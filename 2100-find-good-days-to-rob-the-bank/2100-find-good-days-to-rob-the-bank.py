class Solution:
    def goodDaysToRobBank(self, security: list[int], time: int) -> list[int]:
        #start the arrays
        n = len(security)
        result = []
        left = [0] * n
        right = [0] * n
        #fill the left array
        for i in range(1, n):
            if security[i - 1] >= security[i]:
                left[i] = left[i - 1] + 1
        #fill the right array
        for i in range(n - 2, -1, -1):
            if security[i] <= security[i + 1]:
                right[i] = right[i + 1] + 1
        #loop through the input
        for i in range(time, n - time):
            #if the condition match append the index
            if left[i] >= time and right[i] >= time:
                result.append(i)
        
        return result
