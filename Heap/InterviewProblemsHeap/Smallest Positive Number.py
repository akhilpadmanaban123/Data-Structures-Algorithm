#User function Template for python3   https://practice.geeksforgeeks.org/problems/smallest-positive-missing-number-1587115621/1
import heapq
class Solution:
    
    #Function to find the smallest positive number missing from the array.
    def missingNumber(self,arr,n):
        heap=[]
        for i in arr:
            if i>0:
                heapq.heappush(heap,i)
        
        smallestNumber=1
        
        while heap:
            heapSmall=heapq.heappop(heap)
            if heapSmall>smallestNumber:
                return smallestNumber
            
            if heapSmall==smallestNumber:
                smallestNumber+=1
        return smallestNumber
