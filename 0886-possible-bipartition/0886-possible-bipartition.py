from collections import deque
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        set_A, set_B = set(), set()
        visited = [False]*(n+1)
        
        adj_mat = [[] for _ in range(n+1)]
        for personA, personB in dislikes:
            adj_mat[personA].append(personB)
            adj_mat[personB].append(personA)
        
        for i in range(1,n+1):
            if not visited[i]:
                q = deque([(i, True)])
                while q:
                    person, flag = q.popleft()
                    if flag:
                        if person in set_B:
                            return False
                        set_A.add(person)
                    else:
                        if person in set_A:
                            return False
                        set_B.add(person)
                    visited[person] = True

                    for disliked_person in adj_mat[person]:
                        if not visited[disliked_person]:
                            q.append((disliked_person, not flag))
        
        if len(set_A.union(set_B))==n:
            return True
        return False
        
        