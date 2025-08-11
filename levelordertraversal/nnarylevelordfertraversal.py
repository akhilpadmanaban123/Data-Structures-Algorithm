"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []  # empty tree
        result = [] # final list
        queue = deque()
        queue.append(root)
        while queue:
            level_lst = []   # 
            for _ in range(len(queue)):
                nodes = queue.popleft()
                if nodes:
                    for node in nodes.children:
                        queue.append(node)
                level_lst.append(nodes.val)  # appending the val
            result.append(level_lst)
        return result
        


        # TC : O(n)
        # SC : O(n) for queue
        # where n is the number of nodes in the tree