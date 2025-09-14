from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if key not in self.timeMap:
            return res
        d_list = self.timeMap.get(key)
        l, r = 0, len(d_list) - 1
        while l <= r:
            m = (l + r) // 2
            if d_list[m][1] <= timestamp:
                res = d_list[m][0]
                l = m + 1
            else:
                r = m - 1
        return res

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)