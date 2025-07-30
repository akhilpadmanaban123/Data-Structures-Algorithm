# TC: O(m*n) where m is the number of rows and n is the number of columns
# SC: O(1) - in-place modification of the list


class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
       
        for i in image:
            left,right = 0,len(i)-1
            while left<right:
                i[left],i[right] = 1-i[right],1-i[left]
                left+=1
                right-=1
            if left==right:
                i[left] = 1-i[left]
        return image
