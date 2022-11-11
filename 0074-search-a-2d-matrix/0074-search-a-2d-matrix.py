class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        num_rows, num_cols = len(matrix), len(matrix[0])
        
        def find_idx(st_idx, end_idx, row_num):
            if st_idx > end_idx:
                return False
            mid_idx = (st_idx+end_idx)//2
            if target == matrix[row_num][mid_idx]:
                return True
            if target < matrix[row_num][mid_idx]:
                return find_idx(st_idx, mid_idx-1, row_num)
            else:
                return find_idx(mid_idx+1, end_idx, row_num)
            
            
        def find_row(st_row, end_row):
            if st_row > end_row:
                return -1
            mid_row = (st_row+end_row)//2
            if target >= matrix[mid_row][0] and target <= matrix[mid_row][-1]:
                return mid_row
            if target < matrix[mid_row][0]:
                return find_row(st_row, mid_row-1)
            else:
                return find_row(mid_row+1, end_row)
            
        row_num = find_row(0, num_rows-1)
        if row_num == -1:
            return False
        else:
            return find_idx(0, num_cols-1, row_num)