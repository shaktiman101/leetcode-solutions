#User function template for Python

class Solution:
	def shortest_distance(self, matrix):
		n = len(matrix)
		
		def init_matrix(matrix, repl, val):
		    for i in range(n):
    		    for j in range(n):
    		        if matrix[i][j] == repl:
    		            matrix[i][j] = val
    		            
        init_matrix(matrix, -1, float("inf"))
		
		for via in range(n):
    		for i in range(n):
    		    for j in range(n):
		            matrix[i][j] = min(matrix[i][j], matrix[i][via]+matrix[via][j])
	    
	    init_matrix(matrix, float("inf"), -1)


#{ 
 # Driver Code Starts
#Initial template for Python 

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		matrix = []
		for _ in range(n):
			matrix.append(list(map(int, input().split())))
		obj = Solution()
		obj.shortest_distance(matrix)
		for _ in range(n):
			for __ in range(n):
				print(matrix[_][__], end = " ")
			print()
# } Driver Code Ends