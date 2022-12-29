import heapq
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        res = []
        tasks = sorted([(t[0], t[1], i) for i, t in enumerate(tasks)])
        i = 0
        h = []
        time = tasks[0][0]
        while len(res) < len(tasks):
            while (i < len(tasks)) and (tasks[i][0] <= time):
                heapq.heappush(h, (tasks[i][1], tasks[i][2])) # (processing_time, original_index)
                i += 1
            if h:
                t_diff, original_index = heapq.heappop(h)
                time += t_diff
                res.append(original_index)
            elif i < len(tasks):
                time = tasks[i][0]
        return res
    
    
        for i, task in enumerate(tasks):
            task.append(i)
        tasks = sorted(tasks)
        
        i, ans, n = 1, [], len(tasks)
        curr_time = tasks[0][0]
        task = [tasks[0][1:]]
        heapq.heapify(task)
        
        while i < n:
            proc_time, idx = heapq.heappop(task)
            ans.append(idx)
            curr_time += proc_time
            heapq.heappush(task, tasks[i][1:])
            curr_time = max(curr_time, tasks[i][0])
            i += 1
            while i<n and curr_time >= tasks[i][0]:
                heapq.heappush(task, tasks[i][1:])
                i += 1
        while task:
            _, idx = heapq.heappop(task)
            ans.append(idx)
        return ans
        