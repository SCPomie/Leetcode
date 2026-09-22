class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        #sort the interval
        points.sort()
        #assume res is every arrow for balloon and preEnd is the previous interval
        res, prevEnd = len(points), points[0][1]
        #start at the second interval
        for i in range(1, len(points)):
            
            curr = points[i]
            #if the starting of the current interval is smaller than the ending of the previous interval
            if curr[0] <= prevEnd:
                # decrement the result(num of arrow) and update the prevEnd variabe
                res -= 1
                prevEnd = min(curr[1], prevEnd)
            else:
                #set the preEnd to the current interval if no overlapping
                prevEnd = curr[1]

        return res