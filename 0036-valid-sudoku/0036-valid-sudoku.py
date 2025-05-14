class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols = len(board), len(board[0])
        
        for row in range(rows):
            row_nums = set()
            col_nums = set()
            if row%3 == 0:
                box_nums = [set() for _ in range(3)]
            
            for col in range(cols):
                if board[row][col] in row_nums:
                    return False
                if board[col][row] in col_nums:
                    return False
                if board[row][col] in box_nums[col//3]:
                    return False
                
                if board[row][col] != ".":
                    box_nums[col//3].add(board[row][col])
                    row_nums.add(board[row][col])

                if board[col][row] != '.':
                    col_nums.add(board[col][row])
        
        return True
