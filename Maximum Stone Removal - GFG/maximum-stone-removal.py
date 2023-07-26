#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def maxRemove(self, adj, n):
        rows, cols = 0, 0
        for x, y in adj:
            if x>rows:
                rows = x
            if y>cols:
                cols = y
        rows += 1
        cols += 1
            
        parent = [i for i in range(rows+cols)]
        size = [1 for _ in range(rows+cols)]
        
        def find_uparent(X):
            if X == parent[X]:
                return X
            
            parent[X] = find_uparent(parent[X])
            return parent[X]
        
        
        def union(u, v):
            pu = find_uparent(u)
            pv = find_uparent(v)
            
            if pu == pv:
                return
            
            if size[pu] > size[pv]:
                parent[pv] = pu 
                size[pu] += size[pv]
            else:
                parent[pu] = pv
                size[pv] += size[pu]
        
                
        # same_row = {}
        # same_col = {}
        
        # for x, y in adj:
        #     node = x*col + y
        #     parent[node] = node
        #     size[node] = 1
            
        #     prev_node_same_row = same_row.get(x, None)
        #     prev_node_same_col = same_col.get(y, None)
            
        #     if prev_node_same_row != None:
        #         union(prev_node_same_row[-1], node)
        #         same_row[x].append(node)
        #     else:
        #         same_row[x] = [node]
    
        #     if prev_node_same_col != None:
        #         union(prev_node_same_col[-1], node)
        #         same_col[y].append(node)
        #     else:
        #         same_col[y] = [node]
        
        stoneNodes = {}
        # for row, col in adj:
        #     row_node = row
        #     col_node = rows + col
            
        #     parent[row_node] = row_node
        #     parent[col_node] = col_node
        #     size[row_node] = 1
        #     size[col_node] = 1
        
        for row, col in adj:
            row_node = row
            col_node = rows + col
            union(row_node, col_node)
            stoneNodes[row_node] = 1
            stoneNodes[col_node] = 1
        
        comp = 0
        for node in stoneNodes.keys():
            if find_uparent(node) == node: #parent[node]:
                comp += 1
             
        return n-comp
        
        # comp = 0
        count = 0
        for i in range(rows+cols):
            # print(parent[i], size[i])
            if parent[i] == i and size[i] > 1:
                # comp += 1
                # print(size[i])
                count += size[i] - 1
         
        # print(parent)
        # print(size)
        return count #n-comp
            
            
            

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n = int(input())
        adj = [list(map(int, input().split())) for _ in range(n)]
        ob = Solution()
        res = ob.maxRemove(adj, n)
        print(res)
# } Driver Code Ends