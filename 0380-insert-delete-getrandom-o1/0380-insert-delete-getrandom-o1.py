import numpy as np
class RandomizedSet:

    def __init__(self):
        self.s = set()
        self.arr = []
        self.length = 0

    def insert(self, val: int) -> bool:
        if val in self.s:
            return False
        self.s.add(val)
        self.arr.append(val)
        self.length += 1
        return True

    def remove(self, val: int) -> bool:
        if val in self.s:
            self.s.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        idx = np.random.choice(self.length)
        while self.arr[idx] not in self.s:
            idx = np.random.choice(self.length)
        return self.arr[idx]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()