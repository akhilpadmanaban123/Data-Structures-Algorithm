'''
👇 Let’s go through each elif case one by one:
✅ Case 1: x == y != z
Example: triplet = [2, 2, 4]

x = 2, y = 2, z = 4

Suppose arr = [2, 2, 2, 4, 4]

We want to form combinations like:

scss
Copy
Edit
(2,2,4)
✅ How many ways to pick two 2s?
From 3 twos (2,2,2), how many pairs can we form?

Use combinations formula:

cpp
Copy
Edit
C(count_2, 2) = 3C2 = (3*2)//2 = 3 ways
✅ How many 4s?
count_4 = 2

So total number of [2, 2, 4] combinations:

mathematica
Copy
Edit
= C(3,2) * C(2,1) = 3 * 2 = 6 ways
Code:

python
Copy
Edit
(count_x * (count_x - 1) // 2) * count_z
✅ Case 2: x == z != y
Example: triplet = [3, 1, 3]

x = 3, y = 1, z = 3

Same logic:

Count how many pairs of 3s

Multiply by how many 1s you have

Code:

(count_x * (count_x - 1) // 2) * count_y
✅ Case 3: y == z != x
Example: triplet = [1, 5, 5]

x = 1, y = 5, z = 5

You want to:

Choose 2 fives → C(count_5, 2)

Choose 1 one → count_1

Code:
(count_y * (count_y - 1) // 2) * count_x
Summary Table:
Triplet	Case	Formula
[2,2,4]	x==y!=z	C(count_2,2) * count_4
[3,1,3]	x==z!=y	C(count_3,2) * count_1
[1,5,5]	y==z!=x	C(count_5,2) * count_1
[2,2,2]	x==y==z	C(count_2,3)
[1,2,5]	all different	count_1 * count_2 * count_5




# Time Complexity:
“Even with duplicate triplet skipping, 
the number of unique valid triplets can still be up to O(n²) — for instance, 
if 1000 numbers can each pair with 1000 others to hit the target, that's 1M combinations. 
That’s why m = O(n²).”


# Space Complexity:
“We sort the array in-place (O(1)), but store all unique triplets in a list, 
which in the worst case could be O(n²) in size — so total auxiliary space is O(n²).”
'''


class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        '''
        Given arr and target

Count all triplets (i, j, k) such that:

i < j < k
It’s not about unique value triplets, but about counting valid index-based triplets.

Duplicates matter (same value at different indices).

Need to count combinations accurately, not just detect if they exist.

        '''
        # Put threesum and find the pairs that adds up to target
        # find the combinations and return the sum% (10**9 + 7)


        # threesum array:
        def threeSum(arr, target):
            arr.sort()
            pairs = []
            n = len(arr)
            for i in range(n-2):
                if i>0 and arr[i]==arr[i-1]:
                    continue
                j = i+1
                k = n-1
                while j<k:
                    total = arr[i]+arr[j]+arr[k]
                    if total>target:
                        k-=1
                    elif total<target:
                        j+=1
                    else:
                        pairs.append([arr[i],arr[j],arr[k]])
                        while j<k and arr[j]==arr[j+1]:
                            j+=1
                        while j<k and arr[k]==arr[k-1]:
                            k-=1
                        j+=1
                        k-=1
            return pairs

        #finding occurances
        def findOccr(arr, x, y, z):
            count_x,count_y,count_z = 0,0,0
            for i in arr:
                if i==x:
                    count_x+=1
                elif i==y:
                    count_y+=1
                elif i==z:
                    count_z+=1
            if x!=y and y!=z and x!=z:       # all three are distinct
                return count_x*count_y*count_z
            
            if x==y and y!=z:       # eg [2,2,3]
                return (count_x*(count_x-1)//2)*count_z
            if x==z and y!=z:       # eg [2,3,2]
                return (count_z*(count_z-1)//2)*count_y
            if(y==z and x!=y):      # eg [3,2,2]
                return (count_y*(count_y-1)//2)*count_x

            if (x==y==z):
                return (count_x*(count_x-1)*(count_x-2))//6


        pairs = threeSum(arr,target)  # all pairs adding to target
        #finding occurance
        print(pairs)
        occur = 0
        for i in pairs:         # calling for m triplets 
            occur += findOccr(arr,i[0],i[1],i[2])           # TC = O(m*n)
        return occur%(10**9+7)