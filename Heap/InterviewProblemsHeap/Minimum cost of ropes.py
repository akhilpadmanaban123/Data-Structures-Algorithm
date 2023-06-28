# Algorithm. do minheap/ max heap,  get the minimum first 2 and pop them, add them, then merge to the heap. Again continue it until the size of array is 1

class Solution:
    #Function to return the minimum cost of connecting the ropes.
    def minCost(self,arr,n) :
        import heapq
        dum=[]
        
        heapq.heapify(arr)
        while len(arr)>1:
            a=heapq.heappop(arr)
            b=heapq.heappop(arr)
            dum.append(a+b)
            heapq.heappush(arr,a+b)
        return sum(dum)
