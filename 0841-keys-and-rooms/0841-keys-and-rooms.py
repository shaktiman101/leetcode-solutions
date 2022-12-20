from collections import deque
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = set()
        q = deque([0])
        
        while q:
            room = q.popleft()
            visited.add(room)
            for room_key in rooms[room]:
                if room_key not in visited:
                    q.append(room_key)
                    
        if len(visited) == n:
            return True
        return False