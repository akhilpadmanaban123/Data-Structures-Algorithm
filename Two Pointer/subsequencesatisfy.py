# Two Pointer - Subsequences Satisfy the Given Sum Condition
# LeetCode Problem: https://leetcode.com/problems/subsequences-satisfy-the-given-sum-condition/
# Time Complexity: O(n log n) for sorting, O(n) for the two-pointer traversal
# Space Complexity: O(1) for the two-pointer approach


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10**9+7
        nums.sort()
        comb,res = 0,0
        left,right = 0,len(nums)-1

        pow2 = [1]*len(nums)
        for i in range(1,len(nums)):
            pow2[i] = (pow2[i-1]*2)%MOD

        while left<=right:
            if nums[left]+nums[right]<=target:
                comb=(comb+pow2[right-left])%MOD
                left+=1
            else:
                right-=1
        return comb

            