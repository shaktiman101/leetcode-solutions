class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        n = len(matrix)
        tr, br = 0, n-1
        while tr>=0 and br<n and tr < br:
            midr = (tr+br)//2
            if matrix[midr][0] == target:
                return True
            if target < matrix[midr][0]:
                br = midr-1
            elif target > matrix[midr][-1]:
                tr = midr+1
            else:
                tr, br = midr, midr

        m = len(matrix[0])
        lc, rc = 0, m-1
        while lc>=0 and rc<m and lc <= rc:
            midc = (lc+rc)//2
            if matrix[tr][midc] == target:
                return True
            if target > matrix[tr][midc]:
                lc = midc+1
            else:
                rc = midc-1
        return False