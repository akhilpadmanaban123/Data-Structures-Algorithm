class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        '''
        Each element of nums should be in a pair and max pair sum is minimized
        
        If you pair two biggest numbers together, the sum explodes.
If you pair two smallest numbers together, you leave the biggest ones to pair with only slightly smaller ones, and again the max explodes.

So, the best idea:

Pair the smallest number with the largest, the next smallest with the next largest, etc.
This tends to balance the pair sums, keeping the max in control.


        [2,3,3,5]
        '''

        # sorting the array
        nums.sort()
        left, right = 0, len(nums)-1 # two pointers on on low and another on high   
        max_pair_sum = 0
        while left<=right:
            max_pair_sum = max(max_pair_sum,nums[left]+nums[right])
            left+=1
            right-=1
        return max_pair_sum


        '''
    eg: [3,5,4,2,4,6]
    [2,3,4,4,5,6]
    [8,8,8] - > 8


        '''