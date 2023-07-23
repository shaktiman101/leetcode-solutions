#User function Template for python3

class Solution:
    def accountsMerge(self, accounts):
        n = len(accounts)
        
        parent = [i for i in range(n)]
        size = [1 for _ in range(n)]
        
        def find_uparent(X):
            if X == parent[X]:
                return X
            return find_uparent(parent[X])
            parent[X] = find_uparent(parent[X])
            return parent[X]
            
        def union(u, v):
            pu = find_uparent(u)
            pv = find_uparent(v)
            
            if pu == pv:
                return
            if size[pu] < size[pv]:
                parent[pu] = pv
                size[pv] += size[pu]
            else:
                parent[pv] = pu
                size[pu] += size[pv]
                
        
        account_map = {i:acc for i, acc in enumerate(accounts)}        
        account_node = 0
        email_node_mapping = {}
        node_email_mapping = {}
        
        for account in accounts:
            name, emails = account[0], account[1:]
            for email in emails:
                mapped_node = email_node_mapping.get(email, None)
                if mapped_node == None:
                    email_node_mapping[email] = account_node
                else:
                    union(mapped_node, account_node)
            account_node += 1
                
        
        for email, node in email_node_mapping.items():
            node_parent = find_uparent(node)
            mapped_email = node_email_mapping.get(node_parent, None)
            
            if not mapped_email:
                node_email_mapping[node_parent] = [email]
            else:
                node_email_mapping[node_parent].append(email)
                
        res = []
        for node, email in node_email_mapping.items():
            name = account_map[node][0]
            res.append([name]+sorted(email))
            
        return res
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n = int(input())
        accounts = []
        for i in range(n):
            cntEmails = int(input())
            nameEmails = input().split()
            accounts.append(nameEmails)
        ob = Solution()
        res = ob.accountsMerge(accounts)
        res.sort()
        print('[', end = '')
        for i in range(len(res)):
            print('[', end = '')
            for j in range(len(res[i])):
                if j != (len(res[i]) - 1):
                    print(res[i][j], end = ', ')
                else:
                    print(res[i][j], end='')
            if (i != len(res) - 1):
                print('], ')
            else:
                print(']', end = '')
        print(']')
# } Driver Code Ends