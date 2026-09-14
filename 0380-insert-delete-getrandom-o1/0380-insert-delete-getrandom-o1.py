import random

class RandomizedSet:

    def __init__(self):
        self.array = []
        self.dict = {}

    def insert(self, val: int) -> bool:
        if val not in self.dict:
            self.array.append(val)
            count = len(self.array) - 1
            self.dict[val] = count
            return True
            
        return False

    def remove(self, val: int) -> bool:
        if val in self.dict:
            index = self.dict[val]
            last = self.array[-1]

            self.array[index] = last
            self.dict[last] = index

            self.array.pop()
            del self.dict[val]

            return True
        return False


    def getRandom(self) -> int:
        return random.choice(self.array)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()