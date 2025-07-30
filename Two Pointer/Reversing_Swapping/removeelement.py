class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k,left = 0,0
        while left<len(nums):
            if nums[left]!=val:
                nums[k]=nums[left]  # replace the k with the num
                k+=1
            left+=1
        return k


# TC: O(n)# SC: O(1) - in-place modification of the list
# The list is modified in-place, so no extra space is used for the output.

#Explanation:
# We use two pointers: `k` to track the position of the next valid element,
# and `left` to iterate through the list. If the current element is not equal to `val`, we copy it to the position `k` and increment `k`.
# Finally, we return `k`, which is the new length of the modified list.