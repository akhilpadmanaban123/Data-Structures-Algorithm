# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        # depth of rootnode - 1
        # we have to replace the left and right subtree of the depth and those will become the left-left subtree and right-right subtree of that nodes
        # if depth = 1, we have to create a new rootnode with the val and its left tree would be our entire tree

        if not root:
            return []  # if tree is None
        
        # if depth == 1
        if depth == 1:
            newNode = TreeNode(val)
            newNode.left = root
            return newNode
        
        else:
            count = 0
            queue = deque()
            queue.append(root)
            level = 0
            while queue:
                level_lst = []
                for _ in range(len(queue)):
                    node = queue.popleft()
                    if depth-2 == level:
                        newNodeLeft = TreeNode(val) # Left node with value
                        newNodeRight = TreeNode(val) # right node with value
                        templeft = node.left
                        tempright = node.right
                        node.left = newNodeLeft
                        node.right = newNodeRight
                        newNodeLeft.left = templeft
                        newNodeRight.right = tempright
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                level+=1
        return root
    

    #TC : O(n + v), SC : O(n)