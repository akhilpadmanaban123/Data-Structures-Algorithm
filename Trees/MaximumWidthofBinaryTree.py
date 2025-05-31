# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        queue.append([root,0])  # 0th position
        max_width = 1
        while queue:
            max_width = max(max_width, queue[-1][1]-queue[0][1]+1)
            for _ in range(len(queue)):
                node, position  = queue.popleft()
                if node.left:
                    queue.append([node.left, 2*position+1])
                if node.right:
                    queue.append([node.right, 2*position+2])
        return max_width
            
            
                    
                
        
