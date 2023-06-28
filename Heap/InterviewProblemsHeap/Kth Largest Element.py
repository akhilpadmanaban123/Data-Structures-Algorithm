#Using sort
return sorted(nums)[-k]




#Using Heap
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        result=[]
        for i in nums:
            result.append(-1*i)  # for getting in descending order
        heapify(result) # heapifying the result
        print(result)
        for i in range(k-1):
            heappop(result)
        return -1*heappop(result)



    # n + klog n
