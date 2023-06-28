'''
Height of a heap is O( log n)

left = 2*i
right = 2*i+1
root = floor(i//2)

leafnodes are  = arr[floor(n//2)] to arr[n]
'''

# Min HEapify   
'''
minHeapify function does the adjustment of property, buildMinHeap() creates the heap starting from the last interior node of the tree.
'''
def minHeapify(arr, i):
    left=2*i
    right=2*i+1
    smallest = i
    
    if left<len(arr) and arr[left]<arr[i]:
        smallest=left
    
    if right<len(arr) and arr[right]<arr[smallest]:
        smallest=right 
    
    if smallest!=i:
        arr[i],arr[smallest]=arr[smallest],arr[i]
        minHeapify(arr,smallest)


def buildMinHeap(arr):
    for i in range(len(arr)//2,0,-1):
        minHeapify(arr,i)

arr=[81, 89, 9,11,14,76, 54, 22]
buildMinHeap(arr)
print(arr)
