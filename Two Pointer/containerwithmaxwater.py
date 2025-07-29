class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
        Bruteforce way, 
        Left and Right pointer   
        TC: O(n**2), SC: O(1)
        '''
        n = len(height)
        cur_area, area = 0, 0
        for left in range(n-1):
            for right in range(left+1,n):
                cur_area = min(height[left],height[right])*(right-left)
                area = max(area,cur_area)
        return area
    
# Two pointer approach
# TC: O(n), SC: O(1)
'''
    - left pointer at 0
    - right pointer at n-1
    - whichever is smaller, move that pointer
    - calculate area and update max area  (w*h)
    - continue until left and right pointers meet
    - return max area
'''
class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
        Using two pointers
        '''
        # left and right pointers on left most and rightmost end
        # whichever max height move the opposite pointer
        left, right = 0, len(height)-1
        area = 0
        while left<right:
            cur_height = min(height[left],height[right])
            width = right-left
            area = max(width*cur_height, area)
            if height[right]>height[left]:
                left+=1
            else:
                right-=1
        return area