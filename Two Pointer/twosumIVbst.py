'''
 BST bruteforce + Two Pointer solution 
 TC: O(n), SC: O(n)
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], target: int) -> bool:
        '''
        The sum of two elements in the tree should be target : true 
        Right nodes are greater than left node in BST
        '''
        lst = [] # empty list
        def createList(root):
            if not root:
                return []
            else:
                createList(root.left)
                lst.append(root.val)
                createList(root.right)
            return lst
        
        lst = createList(root) # list containing elemnts
        lst.sort()
        left,right = 0,len(lst)-1
        while left<right:
            if lst[left]+lst[right] >target:
                right-=1
            elif lst[left]+lst[right] <target:
                left+=1
            else:
                return True
        return False
    


    '''
    Using DFS + Hashset for better time complexity
    Using a set to store the elements we have seen so far
    Time Complexity: O(n)
    Space Complexity: O(n)
    '''
    # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        '''
        Using DFS + Hashset
        Same as Two Sum 
        
        Psuedocode:
         have a set= ()
         use a duplicate function:
            inorderTraverse(root, set, k)
                if root is None, returl false
                else
                    if (target-root.val in set):
                        return True
                    else:
                        set.add(root.val)
                    inorderTraverse(root.left)
                    inorderTraverse(root.right)
        
        '''
        s = set()
        def inorder(root):
            if not root:
                return False
            if k-root.val in s:
                return True
            else:
                s.add(root.val)
                return inorder(root.left) or inorder(root.right)
            
        return inorder(root)


        
