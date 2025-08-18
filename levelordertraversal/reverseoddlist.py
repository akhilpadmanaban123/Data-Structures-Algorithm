# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:



    # TC : O(n), SC : O(n)
    # fetch each list level size and the elements in that level.
    # reverse those node values if odd
    # merge the next legvel to queue
    # increament oddevenpointer

    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def swap_list(node):
            left, right = 0, len(node)-1
            while left<right:
                node[left].val,node[right].val = node[right].val,node[left].val
                left+=1
                right-=1
            return node

        if not root:
            return None
        
        counter = 0 # for checking odd even
        queue = deque()
        queue.append(root) 
        while queue:
            level_size = len(queue) # size of the level
            if counter%2!=0:
                temp_list = list(queue)
                res_lst = swap_list(temp_list)  # reverse the list elements 

            # looping level_list times to dequeue
            for _ in range(level_size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            counter+=1
        
        return root
        

        


        # Space optimized solution using DFS
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node1, node2, level):
            if not node1:
                return   # end of tree
            
            if level%2!=0:
                node1.val, node2.val = node2.val, node1.val
            
            dfs(node1.left, node2.right, level+1)
            dfs(node1.right, node2.left, level+1)

            


        if not root:
            return None
        dfs(root.left, root.right, 1)
        return root
        