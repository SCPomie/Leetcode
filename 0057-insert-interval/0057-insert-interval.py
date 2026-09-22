class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        #define the answer list
        ans = []

        # loops through the lists
        for i in range(len(intervals)):
            #checks if the new intervals intercepts before the first interval, if true then add the new intervals to the result
            if newInterval[1] < intervals[i][0]:
                ans.append(newInterval)
                return ans + intervals[i :]
            #chcks if the new intervals intercepts at the end of each interval
            elif newInterval[0] > intervals[i][1]:
                ans.append(intervals[i])
            #else update the new intervals for the intercepting parts
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1]),]
            
        #append the new interval to the answer
        ans.append(newInterval)
        return ans

