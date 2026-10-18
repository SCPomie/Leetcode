from collections import defaultdict

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # Initialize the maximum number of points on a line
        res = 1

        # Select each point as the starting point
        for i in range(len(points)):
            p1 = points[i]

            # Store the number of points sharing each slope
            count = defaultdict(int)

            # Compare p1 with every point after it
            for j in range(i + 1, len(points)):
                p2 = points[j]

                # Handle vertical lines (undefined slope)
                if p2[0] == p1[0]:
                    slope = float("inf")
                else:
                    # Calculate slope between p1 and p2
                    slope = (p2[1] - p1[1]) / (p2[0] - p1[0])

                # Increment the number of points with this slope
                count[slope] += 1

                # Add 1 to include p1 itself
                res = max(res, count[slope] + 1)

        return res