#TC: O(n)
#SC: O(n)


class Solution:
    def validPalindrome(self, s: str) -> bool:
        # two pointers at start and end
        # can delete atmost one character
        # check both ways, (whether we can delete left or right giving palin..)

        left, right = 0, len(s)-1
        while left<right:
            if s[left]!=s[right]:
                skipLeft, skipRight = s[left+1:right+1], s[left:right]
                return (skipLeft==skipLeft[::-1] or
                    skipRight == skipRight[::-1])
            left+=1
            right-=1
        return True