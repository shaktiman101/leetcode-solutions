class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        intervals = sorted(intervals)
        global_start, global_end = intervals[0]
        
        ans = []
        for i in range(1, n):
            start, end = intervals[i]
            if start <= global_end:
                global_start = min(global_start, start)
                global_end = max(global_end, end)
            else:
                ans.append([global_start, global_end])
                global_start = start
                global_end = end
        ans.append([global_start, global_end])
        return ans