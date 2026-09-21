class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        #sort the intervals based on the start
        intervals.sort(key = lambda i : i[0] )
        #initialises the answer list
        ans = [intervals[0]]

        #loops over the intervals with its start and end value
        for start, end in intervals:
            #gets the latest intervals end
            lastEnd = ans[-1][1]
            #if the current interval start is smaller than the latest end value of the intervals
            if start <= lastEnd:
                #set the end value of the latest inverval to the max of current end or the original end
                ans[-1][1] = max(lastEnd, end)
            #otherwise there is a gap, just append the current intervals
            else:
                ans.append([start, end])
        #return the answer list
        return ans
