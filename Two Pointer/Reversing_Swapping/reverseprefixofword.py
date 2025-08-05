class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        left, right = 0, 0
        
        while right<=len(word)-1 and word[right]!=ch:
            right+=1   # finding word
        if right>=len(word):
            return word   # no ch found

        word = list(word)
        while left<=right:
            word[left],word[right] = word[right],word[left]
            left+=1
            right-=1
        return ''.join(word)