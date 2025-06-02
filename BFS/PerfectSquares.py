class Solution:
    def numSquares(self, n: int) -> int:
        
        # find all perfect squares thats <=n
        pfct_squares= []
        for i in range(1, int(math.sqrt(n)+1)):
            pfct_squares.append(i*i)
        
        queue = deque()
        queue.append([n,0])  # remaining value, steps
        visited = set()
        while queue:
            remaining, steps = queue.popleft()
            if remaining == 0:
                return steps
            for sq in pfct_squares:
                new_rem = remaining - sq
                if new_rem <0:
                    break
                if new_rem not in visited:
                    visited.add(new_rem)
                    queue.append([new_rem,steps+1])
        

______________________________________________________________

Explanation:
Let’s walk step-by-step through the BFS flow for the problem:

🧩 Problem:
Find the minimum number of perfect squares that sum to n = 12.

✅ Step 1: Precompute Perfect Squares ≤ 12
Perfect squares ≤ 12:

1² = 1

2² = 4

3² = 9

So:

squares = [1, 4, 9]
✅ Step 2: Initialize BFS
We start with:

queue = deque([(12, 0)])   # (current value, steps)
visited = set()
🔁 Step-by-step BFS Expansion:
🔹 Level 0:
(12, 0)
→ Try subtracting perfect squares:

Square	12 - square	New Node
1	11	(11, 1)
4	8	(8, 1)
9	3	(3, 1)

queue = [(11,1), (8,1), (3,1)]
🔹 Level 1:
Current: (11, 1)

Square	11 - square	New Node
1	10	(10, 2)
4	7	(7, 2)
9	2	(2, 2)

Current: (8, 1)

Square	8 - square	New Node
1	7 (already in queue)	
4	4	(4, 2)
9	-1	ignore

Current: (3, 1)

Square	3 - square	New Node
1	2 (already in queue)	
4, 9	too big	ignore

python
Copy
Edit
queue = [(10,2), (7,2), (2,2), (4,2)]
🔹 Level 2:
Now from (10, 2):

Square	Result	New Node
1	9	(9, 3)
4	6	(6, 3)
9	1	(1, 3)

And so on...

Eventually you’ll reach:

(0, 3) from (4, 2) → because 4 - 4 = 0

