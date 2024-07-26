
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity.

LEETCODE 704


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)-1
        while low<=high:
            mid = (low+high)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                high = mid-1
            else:
                low = mid+1
        return -1
