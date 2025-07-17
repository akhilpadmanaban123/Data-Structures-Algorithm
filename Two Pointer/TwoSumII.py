https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Thinking Process:
        '''
        create an empty list
        traverse through the list of numbers
        subtract the target - nums[i] and check if the result is there in the empty list
        if not present, append [nums[i], ] in the list 
        if present, return the second element's position from that empty list along with the current index+1

        eg:
        [2,7,11,15]  target = 9

        val = 9-2 , val not in emptyList ( [2,])
        val = 9-7, val in emptyList( return [1,2])
        '''


        # Brute Force Approach
        # Using a nested loop to check each pair of numbers.
        # TC: O(n^2), SC : O(n)
        resList = []
        for i in range(len(numbers)):
            val = target - numbers[i]
            if val not in resList:
                resList.append(numbers[i])
            else:
                return [resList.index(val)+1, i+1]
        return [0,0]
        
        # HashMap Approach
        # Using a dictionary to store the numbers and their indices.
        # TC: O(n), SC = O(n)
        dic = dict()
        for i in range(len(numbers)):
            val = target-numbers[i]
            if val not in dic:
                dic[numbers[i]] = i
            else:
                return [dic[val]+1, i+1]
        return [0,0]
        

        # Two Pointer Approach
        # The list is sorted, so we can use two pointers to find the target sum.
        #TC = O(n), SC = O(1)
        
        leftPtr, rightPtr = 0, len(numbers)-1

        while leftPtr<rightPtr:
            if numbers[leftPtr]+numbers[rightPtr] == target:
                return [leftPtr+1, rightPtr+1]
            elif numbers[leftPtr]+numbers[rightPtr] <target:
                leftPtr+=1
            else:
                rightPtr-=1
        return [0,0]

        
twoSum = Solution().twoSum(numbers=[2,7,11,15], target=9)
print(twoSum)  # Output: [1, 2]