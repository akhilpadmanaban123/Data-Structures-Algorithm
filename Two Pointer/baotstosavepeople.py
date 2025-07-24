# Greedy + Two Pointer - Boats to Save People
# LeetCode Problem: https://leetcode.com/problems/boats-to-save-people/
# Time Complexity: O(n log n) for sorting, O(n) for the two-pointer traversal

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        '''
        - people array is given, each elemt is the weight of the person. 
        person are the indexes.
        - infinite numnber of boats are given, each both can carry max weight of limit.
        - 1 2 2 3  limit = 3
        boat = (1),(2),(2),(1,2),(1,2),(3).

        but its given that we have to return min number of boats needed to carry everyone here.

        eg2:

        [3,3,4,5]

        left, right = 3,5
        3+5 = 8 >5:
        [3,3,4]
        3+4 = 7>5
        [3,3]
        3+3 >5:
        [3]
        3<5: -->1
        '''
        people.sort()       
        left,right = 0,len(people)-1
        boats = 0
        while left<=right:
            if people[left]+people[right]<=limit:
                left+=1
                right-=1
            else:
                right-=1  # heaviest person goes alone
            boats+=1
            
        return boats