class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        lost_no_match = set()
        lost_one_match = set()
        rest = set()
        
        for winner, looser in matches:
            if looser in lost_no_match:
                lost_no_match.remove(looser)
                lost_one_match.add(looser)
            elif looser in lost_one_match:
                lost_one_match.remove(looser)
                rest.add(looser)
            elif looser not in rest:
                lost_one_match.add(looser)
            if winner not in rest and winner not in lost_one_match:
                lost_no_match.add(winner)
        return [sorted(lost_no_match), sorted(lost_one_match)]
            