class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        
        
        def dfs(cur):
            if cur not in visitedStack:
                visitedStack.append(cur)
                for i in adj[cur]:
                    dfs(i)
        
        visitedStack=[]
        dfs(0)
        return visitedStack
