#User function Template for python3

from typing import List
from queue import Queue
from collections import deque
class Solution:
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        queue=deque()
        visited=[]
        if V!=0:
            queue.append(0)
            visited.append(0)
        
        while queue:
            m=queue.popleft()
            for i in adj[m]:
                if i not in visited:
                    visited.append(i)
                    queue.append(i)
        return visited
