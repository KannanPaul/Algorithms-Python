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

def bubbleSort(arr: List[int], n: int):
    n = len(arr)
    for i in range(n):
        for j in range(n - i -1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            
    return arr

