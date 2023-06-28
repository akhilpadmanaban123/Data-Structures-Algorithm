def heapSort(arr):
    # first do a max heap from the unordered array
    # O(n)
    maxHeap(arr)
    
    # Then apply heapify property and swapping of root and last node
    # (O ( log n))
    for i in range(len(arr)-1,0,-1):
        arr[0],arr[i]=arr[i],arr[0]
        heapify(arr,i,0)

def heapify(arr,n,i):
    left= 2*i
    right=2*i+1
    largest= i
    
    if left<n and arr[left]>arr[i]:
        largest=left
    
    if right<n and arr[right]>arr[left]:
        largest=right
    
    if largest!=i:
        arr[i],arr[largest]=arr[largest],arr[i]
        heapify(arr,n,largest)
        

def maxHeap(arr):
    for i in range(len(arr)//2,0,-1):
        heapify(arr,len(arr),i)


arr=[81, 89, 9,11,14,76, 54, 22]
heapSort(arr)
print(arr)
