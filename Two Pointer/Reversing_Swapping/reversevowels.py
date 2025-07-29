class Solution:
    def reverseVowels(self, s: str) -> str:
        '''
        IceCreAm

        vowels are : I_e__eA_
        vowels after reverse: A_e__eI_
        Answer : AceCreIm
        '''
        #Pseudo
        # 1. if both pointers are vowels, swap and update pointers
        # 2. If one pointer is vowel, keep it and update the other and viseversa

        left, right = 0, len(s)-1
        vowels = 'AEIOUaeiou'
        s = list(s)
        while left<right:
            if s[left] in vowels and s[right] in vowels:
                s[left],s[right] = s[right],s[left]
                left+=1
                right-=1
            elif s[left] in vowels:
                right-=1
            else:
                left+=1
        return ''.join(s)
    

#TC: O(n), SC: O(n) - for list conversion
#Note: In-place modification is not required here, so we can return a new string.