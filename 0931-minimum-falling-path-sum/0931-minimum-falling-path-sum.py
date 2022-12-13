class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        A = matrix
        for i in range(1,len(A)):
            for j in range(len(A[0])):

                #edge cases are first column and last column which only have two paths from above
                if j == 0:
                    A[i][j]  = min((A[i][j] + A[i - 1][j]), (A[i][j] + A[i - 1][j + 1]) )

                elif (j == len(A[0]) - 1):
                    A[i][j]  = min((A[i][j] + A[i - 1][j]), (A[i][j] + A[i - 1][j - 1]) )

                #every other column will have three paths coming from above
                else:
                    A[i][j] = min(A[i][j] + A[i - 1][j],A[i][j] + A[i - 1][j + 1], A[i][j] + A[i - 1][j - 1])

        # Now that minimum falling sums for each value at the bottom row have been computer
        # We can just take the min of the bottow row to get the smallest overall path sum 
        return min(A[len(A) - 1])


        n = len(matrix)
        
        def solve2(row, col):
            if row == n-1:
                return matrix[row][col]
            
            for j in range(n):
                c1 = float('inf')
                if j>0:
                    c1 = solve(row+1, j-1)
                c2 = solve(row+1, j)
                c3 = float('inf')
                if j<n-1:
                    c3 = solve(row+1, j+1)
                return matrix[row][col] + min(c1, c2, c3)
            
        def solve(row, col):
            if row >= n or col < 0 or col >= n:
                return 101
            
            n1 = solve(row+1, col)
            n2 = solve(row+1, col-1)
            n3 = solve(row+1, col+1)
            # if float('inf') in [n1, n2, n3]:
            #     return matrix[row][col]
            # print(n1, n2, n3)
            return matrix[row][col] + min(n1, n2, n3)
            
        min_ = float('inf')
        for j in range(n):
            min_ = min(min_, solve(0, j))
            print(min_)
        return min_