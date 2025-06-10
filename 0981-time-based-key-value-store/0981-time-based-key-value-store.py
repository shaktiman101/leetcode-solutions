class TimeMap:

    def __init__(self):
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashmap:
            self.hashmap[key] = []
        self.hashmap[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        timestamp_vals = self.hashmap.get(key, [])
        if not timestamp_vals:
            return ""
        if timestamp_vals[0][0] > timestamp:
            return ""
        if timestamp_vals[-1][0] <= timestamp:
            return timestamp_vals[-1][1]
        
        min_timestamp = (0, "")
        left, right = 0, len(timestamp_vals)-1
        while left<=right:
            mid = (left+right)//2
            if timestamp_vals[mid][0] <= timestamp:
                left = mid+1
                if min_timestamp[0] < timestamp_vals[mid][0]:
                    min_timestamp = timestamp_vals[mid]
            else:
                right = mid-1
        return min_timestamp[-1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)