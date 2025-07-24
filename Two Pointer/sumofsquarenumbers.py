'''
First Solution: Two Pointer - Sum of Square Numbers
LeetCode Problem: https://leetcode.com/problems/sum-of-square-numbers/
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        We have a non -neg integer given as c
        we have to find two numbers <=c such that a**2 + b**2 is c

        Mindvoice:
        - lay down till c
            c = 5
            [1,2,3,4,5]

            two pointers one at 0 and rght at end..
            1**2 + 5**2 > target:
            right--
            else left ++
            if value is found, return True, else False
        

        lst = [1]*(c+1)
        for i in range(c+1):
            lst[i] = i
        print(lst)
        left, right = 0, len(lst)-1
        while left<=right:
            if (lst[left]**2 + lst[right]**2) == c:
                return True
            elif (lst[left]**2 + lst[right]**2) < c:
                left+=1
            else:
                right-=1
     return False
     
     Above solution exceeds time limit
     
     '''

# no need of an external list, we can use the range function directly
class Solution: 
    def judgeSquareSum(self, c: int) -> bool:
        left, right = 0, int(c**0.5)
        while left <= right:
            total = left**2 + right**2
            if total == c:
                return True
            elif total < c:
                left += 1
            else:
                right -= 1
        return False