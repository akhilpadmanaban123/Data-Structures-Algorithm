class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        '''
        [4,2,5,7]
           o
        [2,4,5,7]   -- >   [2,5,4,7]
           o e                o      e
        '''
        even,odd = 0,1
        n = len(nums)
        while even<n and odd<n:
            if nums[even]%2==0:
                even+=2
            elif nums[odd]%2==1:
                odd+=2
            else:
                nums[even],nums[odd]=nums[odd],nums[even]
                even+=2
                odd+=2
        return nums
    
# Output: [4, 5, 2, 7]
print(Solution().sortArrayByParityII([4,2,5,7]))  # Output: [4, 5, 2, 7]
# Time Complexity: O(n)
# Space Complexity: O(1)