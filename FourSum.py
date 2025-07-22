class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        '''
        Mind voice:
            - Similar to 3 sum problem, we have one more 4th element. 
            - Threesum we used i as the main top loop , j and k as inner pointers from i+1 and len(nums)-1
            - 
        '''
        n = len(nums)
        nums.sort() 
        quad = [] # result
        for i in range(n-3):
            if i>0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, n-2):
                if j>i+1 and nums[j] == nums[j-1]:
                    continue
                k, l = j+1, n - 1   # k - third pointer , l = fourth pointer
                while k<l:
                    total = nums[i]+nums[j]+nums[k]+nums[l]
                    if total > target :
                        l-=1
                    elif total <target:
                        k+=1
                    else:
                        quad.append([nums[i],nums[j],nums[k],nums[l]])
                        while k<l and nums[k]==nums[k+1]:
                            k+=1
                        while k<l and nums[l] == nums[l-1]:
                            l-=1
                        k += 1
                        l -= 1

        return quad
    



    or 

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
                        if nums[i] * k > target:
                            break
                        if nums[-1] * k < target:
                            continue
                        if i>start and nums[i]==nums[i-1]:
                            continue  # skipping starting duplicates
                        
                        target2 = target-nums[i]
                        for subset in kSum(nums, target2, k-1, i+1):
                            result.append([nums[i]]+subset)
                return result
        
        nums.sort() # sort thhe array first
        return kSum(nums, target, 4, 0)  # starting is 0 and sum questio is 4
    
    '''
    So for general kSum:
🔸 Time Complexity: O(n^(k-1))

For 4Sum:

🔹 TC = O(n³)

🔸 Space Complexity: O(k)

1. Sorting the array:
O(n) (or O(log n) if in-place depending on sort implementation)

2. Recursive call stack:
Depth = k → O(k)

3. Result storage:
Number of valid k-tuples = O(n^(k-1)) in worst-case (e.g., all zeros or all duplicates)

So overall:
🔸 Space Complexity = O(n^(k-1)) for results
🔹 + O(k) for recursion stack


    k	Time Complexity	Space Complexity
2Sum	O(n)	O(1) or O(n) for result
3Sum	O(n²)	O(n) for result
4Sum	O(n³)	O(n²) for result
kSum	O(n^(k-1))	O(n^(k-1))
    '''
