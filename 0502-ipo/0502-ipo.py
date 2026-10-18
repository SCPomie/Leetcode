import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # Max-heap to store profits of affordable projects
        maxProfit = []

        # Min-heap sorted by capital requirements
        minCapital = [(c, p) for c, p in zip(capital, profits)]
        heapq.heapify(minCapital)

        # Complete at most k projects
        for _ in range(k):

            # Move all affordable projects into the max-profit heap
            while minCapital and minCapital[0][0] <= w:
                c, p = heapq.heappop(minCapital)
                heapq.heappush(maxProfit, -p)

            # Stop if no projects can be started
            if not maxProfit:
                break

            # Complete the most profitable affordable project
            w += -heapq.heappop(maxProfit)

        return w