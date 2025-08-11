# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []  # empty tree
        result = []
        queue = deque()  # double ended queue
        queue.append(root)  # root as the first node
        while queue:
            lst = [] # storing the sublists
            for _ in range(len(queue)):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                lst.append(node.val)
            result.append(lst)
        return result