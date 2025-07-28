class Solution:
    def trap(self, height: List[int]) -> int:

        '''
        my first mindthought:
            - start two pointers (0, n-1)
            -[0..1] - 0
            -[1..1] - 9
            -[]

        '''

        # Brute force Solution : 
            # - TC : O(n**2), SC : O(1)
        # water_at_i = min(max_water at left, max_water at right) - height[i]
        '''
        max_water = 0
        for i in range(len(height)):
            max_left = max(height[:i+1])
            max_right = max(height[i:])
            max_water += min(max_left,max_right)-height[i]
        return max_water
            '''
        left,right = 0,len(height)-1
        left_max,right_max = 0,0
        water = 0 # total water space
        while left<right:
            if height[left]<height[right]:
                left_max = max(height[left],left_max)
                water += left_max - height[left]
                left+=1
            else:
                right_max = max(height[right],right_max)
                water += right_max - height[right]
                right-=1
        return water

        


        