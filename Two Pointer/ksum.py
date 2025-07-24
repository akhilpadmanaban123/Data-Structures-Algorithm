class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def kSum(nums,target, k, start):
                result = [] # final result
                if k == 2:
                    start, end = start, len(nums)-1
                    while start<end:
                        total = nums[start]+nums[end]
                        if total >target:
                            end-=1
                        elif total <target:
                            start+=1
                        else:
                            result.append([nums[start],nums[end]])
                            start+=1
                            end-=1
                            while start<end and nums[start]==nums[start-1]:
                                start+=1
                            while start<end and nums[end]==nums[end+1]:
                                end-=1
                else:
                    for i in range(start, len(nums)-k+1):
                        if i>start and nums[i]==nums[i-1]:
                            continue  # skipping starting duplicates
                        
                        target2 = target-nums[i]
                        for subset in kSum(nums, target2, k-1, i+1):
                            result.append([nums[i]]+subset)
                return result
        
        nums.sort() # sort thhe array first
        return kSum(nums, target, k, 0)  # starting is 0 and sum questio is 4