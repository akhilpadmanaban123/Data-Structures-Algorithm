class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        Two pointer approach comes to my mind at first hehe
        check w.r.t lowercase alphanum.
        if non alphanum are found, we have to skip that pointer
        '''
        left,right = 0, len(s)-1
        while left<right:
            if s[left].isalnum():
                a = s[left].lower()
            if s[right].isalnum():
                b = s[right].lower()
            if not s[left].isalnum():
                left+=1
                continue
            if not s[right].isalnum():
                right-=1
                continue
            if a!=b:
                return False
            else:
                left+=1
                right-=1
        return True
            

#TC: O(n), SC: O(1)