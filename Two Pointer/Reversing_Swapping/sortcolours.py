# My mind was fresh as I found out we have to use dutch national flag problem to solve this problem
# TC: O(n)
# SC: O(1) - in-place modification of the list

#Solution:
# We use three pointers: `low`, `mid`, and `high`.
# `low` tracks the position to place the next 0,
# `mid` is the current element being examined, and `high` tracks the position to place the next 2.
# If `nums[mid]` is 0, we swap it with `nums[low]` and increment both `low` and `mid`.
# If `nums[mid]` is 1, we simply increment `mid`.
# If `nums[mid]` is 2, we swap it with `nums[high]` and decrement `high`.



class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        increment mid while mid<=high"
  	if arr[mid] == 0
  		swap mid, low
  		low+=1
  		mid+=1
  	if arr[mid]==1:
  		mid+=	
  	if arr[mid]==2:
  		swap mid,high
  		high-=1
        '''
        low,mid,high=0,0,len(nums)-1
        while mid<=high:
            if nums[mid]==0:
                nums[mid],nums[low]=nums[low],nums[mid]
                low+=1
                mid+=1
            elif nums[mid]==1:
                mid+=1
            else:
                nums[mid],nums[high] = nums[high], nums[mid]
                high-=1
        return nums