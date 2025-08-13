# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #0,2,4 ... will be proper and rest are zigged
        # if no root present, return empty tree
        # BFS traverses through levels will be an optimal approach
        # TC : O(ndoes + vertices), SC : O(nodes)

        if not root:
            return []  # empty ]
        
        result = [] # final result
        queue = deque()  # a two sided empty queue
        queue.append(root)  # root as the first node
        count = 0
        while queue:
            level_lst = []  # to store level lists
            count+=1
            for _ in range(len(queue)):
                nodes = queue.popleft()  # poping the first pushed node
                if nodes.left:
                    queue.append(nodes.left)
                if nodes.right:
                    queue.append(nodes.right)
                level_lst.append(nodes.val)
            if count%2==0:
                result.append(level_lst[::-1])
            else:
                result.append(level_lst)
        return result


#TC : O(n + v), SC : O(n)