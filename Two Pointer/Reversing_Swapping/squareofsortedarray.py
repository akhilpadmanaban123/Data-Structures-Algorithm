# The problem is to return a new list containing the squares of each number in the input list, sorted in non-decreasing order.
# Intuition states that we can use a two-pointer approach to achieve this efficiently.
# Already the list is sorted, so we can use two pointers to compare the squares of the numbers at the two ends of the list.
# The larger square will be placed at the end of the new list, and we will move the pointer accordingly.
# This way, we can fill the new list from the back to the front, ensuring that we maintain the sorted order.
# TC: O(n) where n is the length of the input list
# SC: O(n) for the output list, but the input list is not modified in

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        arr = [0,]*len(nums)
        j = len(arr)-1  # pointer in arr
        left,right = 0, len(nums)-1
        while left<=right:
            leftq= nums[left]**2
            rightq = nums[right]**2
            if leftq>rightq:
                arr[j] = leftq
                left+=1
            else:
                arr[j]=rightq
                right-=1
            j-=1
        return arr

      


        