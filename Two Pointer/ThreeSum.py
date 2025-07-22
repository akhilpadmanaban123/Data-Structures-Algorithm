# Time Complexity: O(n^2)
# Space Complexity: O(k)


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        Mindvoice:
         There are a list of elements which are not sorted. We have to find all the triplets that adds up and gives 0.
         - i,j,k should be different numbers. 
         - duplicate triplets shouldnt exist.
         - There should be atleast three numbers.

        Methods coming into mind:
         - Pointer solutions. ( Using three pointers )
         - 
        '''
        triplets = []
        # first sort the array
        nums.sort()

        for i in range(len(nums)):
            if nums[i] == nums[i-1] and i>0:
                continue
            j = i+1
            k = len(nums)-1  #k at last index
            while j<k:  # j from second i+1th index
                summ = nums[i]+nums[j]+nums[k]
                if summ>0:
                    k-=1
                elif summ<0:
                    j+=1
                else:
                    triplets.append([nums[i],nums[j],nums[k]])
                    j+=1
                    while nums[j]== nums[j-1] and j<k:
                        j+=1
        return triplets

                


        