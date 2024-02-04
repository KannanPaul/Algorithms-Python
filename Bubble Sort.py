'''
Problem statement
You are given an integer array 'arr' of size 'N'.
You must sort this array using 'Bubble Sort'.

Note: Change in the input array itself. You don't need to return or print the elements.

Example:
Input: ‘N’ = 7
'arr' = [2, 13, 4, 1, 3, 6, 28]
Output: [1 2 3 4 6 13 28]

Explanation: After applying bubble sort on the input array, the output is [1 2 3 4 6 13 28].
'''

# Solution 1:
# Time Complexity - O( N ^ 2 ), where 'N' is the array ‘arr’ size. In the worst case, we have to do n^2 iterations on the array ‘arr’, Hence the time complexity is O( N ^ 2 ).      
# Space Complexity - O( 1 ).
# Approach : To sort our array using Bubble Sort, we will repeatedly check the adjacent elements in our array, and if they are in the wrong order (i.e., the previous element is greater than the next element), we will swap both of them, we will do this until our array is sorted.

def bubbleSort(arr: List[int], n: int):
    n = len(arr)
    for i in range(n):
        for j in range(n - i -1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            
    return arr


# Solution 2:
# Time Complexity: O(n*n)
# Auxiliary Space: O(n)

def recursiveBubbleSort(arr, n):
    if n == 1:
        return
    swap = 0
    for i in range(n-1):
       if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i] 
            swap = 1
    if swap == 0:
        return
    recursiveBubbleSort(arr, n-1)

recursiveBubbleSort(arr, n)
