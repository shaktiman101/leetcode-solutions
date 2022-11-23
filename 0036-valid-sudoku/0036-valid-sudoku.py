# from collection import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = set()
        col_set = set()
        sub_boxes = {}
        
        def test(i,j):
            print(i, j)
            print(row_set)
            print(col_set)
            print(sub_boxes)
            
        for i in range(3):
            for j in range(3):
                sub_boxes[(i,j)]=set()
        
        
        for i in range(9):
            row_set.clear()
            col_set.clear()
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in col_set:
                        # test(i,j)
                        return False
                    col_set.add(board[i][j])
                    if board[i][j] in sub_boxes[(i//3,j//3)]:
                        # test(i,j)
                        return False
                    sub_boxes[(i//3,j//3)].add(board[i][j])
                    
                if board[j][i] != '.':
                    if board[j][i] in row_set:
                        # test(i,j)
                        return False
                    row_set.add(board[j][i])
                    
                    
        return True
        