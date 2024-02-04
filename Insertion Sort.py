'''
 Problem statement

You are given an integer array 'arr' of size 'N'.


You must sort this array using 'Insertion Sort' without & with recursion.


 Note:

Change in the input array itself. You don't need to return or print the elements.

Example:

Input: ‘N’ = 7
'arr' = [2, 13, 4, 1, 3, 6, 28]

Output: [1 2 3 4 6 13 28]

Explanation: After applying insertion sort on the input array, the output is [1 2 3 4 6 13 28].
'''

# Solution 1: Insertion Sort
# Time Complexity - O(N^2), where ‘N’ is the number of length of array.
# Space Complexity - O(1)

def insertionSort(arr):
    n = len(arr)

    for i in range(n):
        j = i
        while (j > 0) and (arr[j-1] > arr[j]):
            arr[j - 1], arr[j] = arr[j], arr[j-1]
            j = j - 1
    return arr

# Solution 2: Recusrion Insertion Sort

'''
# Time Complexity -  O( N ^ 2 ), where 'N' is the array ‘arr’ size.

In the worst case, we have to do n^2 recursive call on the array ‘arr’,

Hence the time complexity is O( N ^ 2 ).      

# Space Complexity - O( N ), where 'N' is the array ‘arr’ size.
 
We are using O(N) auxiliary stack space,

Hence the space complexity is O( N ).
'''

def insertionSortRecursion(arr, i, n):
    if i == n:
        return
    j = i
    while j > 0 and arr[j-1] > arr[j]:
        arr[j-1], arr[j] = arr[j], arr[j-1]
        j = j - 1
    return insertionSortRecursion(arr, i+1,n)

insertionSortRecursion(arr, 0, len(arr))
