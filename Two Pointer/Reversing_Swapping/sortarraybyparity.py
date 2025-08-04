class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left,right=0,0
        while right<=len(nums)-1:
            if nums[right]%2==0:
                nums[left],nums[right]=nums[right],nums[left]
                left+=1
            right+=1
        return nums


# TC: O(n) where n is the length of the input list place.
# SC: O(1) since we are modifying the input list in place.