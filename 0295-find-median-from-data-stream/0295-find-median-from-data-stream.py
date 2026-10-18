import heapq

class MedianFinder:
    def __init__(self):
        # Initialise two heaps, small (max heap) and large (min heap)
        # small stores the smaller half, large stores the larger half
        # Both heaps should have equal size or differ by at most 1
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        # If num is larger than the smallest element in large, add it to large
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            # Otherwise add it to small (negative values for max heap)
            heapq.heappush(self.small, -1 * num)

        # If small has more than 1 extra element, move its largest to large
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # If large has more than 1 extra element, move its smallest to small
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        # If small has more elements, return the largest element in small
        if len(self.small) > len(self.large):
            return -1 * self.small[0]

        # If large has more elements, return the smallest element in large
        elif len(self.large) > len(self.small):
            return self.large[0]

        # If both heaps have equal size, return the average of their top elements
        return (-1 * self.small[0] + self.large[0]) / 2.0

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()