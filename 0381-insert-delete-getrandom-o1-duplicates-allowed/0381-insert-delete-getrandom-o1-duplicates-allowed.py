from collections import defaultdict
import random
class RandomizedCollection:

    def __init__(self):
        self.d = defaultdict(list)
        self.arr = []
        self.length = 0

    def insert(self, val: int) -> bool:
        res = False
        if val not in self.d:
            res = True
        self.d[val].append(self.length)
        self.arr.append(val)
        self.length += 1
        return res

    def remove(self, val: int) -> bool:
        
        if val not in self.d:
            return False
        idxs = self.d[val]
        
        if len(idxs) == 1:
            idx = idxs[0]
            self.arr[idx], self.arr[-1] = self.arr[-1], self.arr[idx]
            
            indices = self.d[self.arr[idx]]
            for i, tmp_idx in enumerate(indices):
                if self.length-1 == tmp_idx:
                    indices[i] = idx
                    break
            
            self.d[self.arr[idx]] = indices
            self.arr.pop()
            self.d.pop(val)
                
        else:
            self.arr[idxs[-1]], self.arr[-1] = self.arr[-1], self.arr[idxs[-1]]
            indices = self.d[self.arr[idxs[-1]]]
            for i, tmp_idx in enumerate(indices):
                if self.length-1 == tmp_idx:
                    indices[i] = idxs[-1]
                    break
            
            self.d[self.arr[idxs[-1]]] = indices
            
            self.arr.pop()
            self.d[val].pop()
        
        self.length -= 1
        return True
        

    def getRandom(self) -> int:
        idx = int(random.random() * self.length)
        return self.arr[idx]
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()