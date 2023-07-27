#User function Template for python3


#Function to determine if graph can be coloured with at most M colours such
#that no two adjacent vertices of graph are coloured with same colour.
def graphColoring(graph, k, V):
    color = [-1]*V
    
    def is_valid(node, c):
        for adj_node, is_connected in enumerate(graph[node]):
            if is_connected and color[adj_node] == c:
                return False
        return True
        
    def backtrack(node):
        if node == V:
            return True

        # for adj_node, is_connected in enumerate(graph[node]):
        #     if not is_connected or color[adj_node] != -1:
        #         continue
        for c in range(k):
            if is_valid(node, c):
                color[node] = c
                if backtrack(node+1):
                    return True
                color[node] = -1
        return False

    # color[0] = 0
    return backtrack(0)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while(t>0):
        V = int(input())
        k = int(input())
        m = int(input())
        list = [int(x) for x in input().strip().split()]
        graph = [[0 for i in range(V)] for j in range(V)]
        cnt = 0
        for i in range(m):
            graph[list[cnt]-1][list[cnt+1]-1]=1
            graph[list[cnt+1]-1][list[cnt]-1]=1
            cnt+=2
        if(graphColoring(graph, k, V)==True):
            print(1)
        else:
            print(0)

        t = t-1

# } Driver Code Ends