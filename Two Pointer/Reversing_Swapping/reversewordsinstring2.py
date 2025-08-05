class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()  # splitting words to list 
        for i,word in enumerate(s):
            s[i] = word[::-1]
        return ' '.join(s)
        