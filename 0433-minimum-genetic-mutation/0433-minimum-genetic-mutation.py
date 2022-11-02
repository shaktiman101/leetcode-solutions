class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
#         bank = set(bank)
#         n, count = len(start), 0
        
#         start_diff, end_diff = [], []
#         for i in range(n):
#             if start[i] != end[i]:
#                 start_diff.append(start[i])
#                 end_diff.append(end[i])
        
#         start = [*start]
#         end = [*end]
        
#         def solve(n):
#             if n < 1:
#                 return 0
#             tmp = solve(n-1)
#             if start[n-1] != end[n-1]:
#                 start[n-1] = end[n-1]
#                 if start in bank:
#                     tmp += 1
#                 else:
#                     return
#             else:
#                 return tmp
#         solve(n)

        ### check to see if a and b are neighbors
        ### i.e., a and b only differ by one character
        def checkNeighbor(a,b):
            return sum([1 for i in range(len(a)) if a[i]!=b[i]]) == 1
        
        ### initialize the q with start and 0 mutations
        q = deque([[start,0]])
        ### initialize the visited set with start
        visited = {start}
        while q:
            cur, mutations = q.popleft()
            ### if cur == end, we are done
            if cur == end:
                return mutations
            ### go through all gene mutations from the bank
            for nei in bank:
                ### check if nei is a valid neighbor and if we have visited it before
                ### if not, we add it to the visited, add it to the q with mutations+1
                if checkNeighbor(cur,nei) and nei not in visited:
                    visited.add(nei)
                    q.append([nei,mutations+1])
        ### if we don't reach the end, there is no such a mutation, return -1
        return -1
            
            
        