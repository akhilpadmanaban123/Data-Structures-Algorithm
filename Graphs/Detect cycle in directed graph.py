class Graph:
    def __init__(self, v):
        self.v=v
        self.adj=[0]*v
        for i in range(self.v):
            self.adj[i]=[]
    
    def addEdge(self, i, j):
        self.adj[i].append(j)
    
    def isCyclic(self):
        visited=[False]*self.v
        helper=[False]*self.v
        for i in range(self.v):
            if visited[i]==False:
                ans=self.DFS(i,visited,helper)
                if ans==True:
                    return True
        return False
    
    def DFS(self, i, visited, helper):
        visited[i]=True
        helper[i]=True
        neighbours=self.adj[i]
        for k in range(len(neighbours)):
            curr=neighbours[k]
            if helper[curr]==True:
                return True
            if visited[curr]==False:
                ans=self.DFS(curr,visited,helper)
                if ans==True:
                    return True
        helper[i]=False
        return False
    
n=4
g=Graph(n)
g.addEdge(0,1)
g.addEdge(1,0)
if g.isCyclic()==1:
    print('Graph has a cycle')
else:
    print('Graph has no cycle')
                
