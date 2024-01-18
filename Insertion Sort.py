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

# Solution 1: 
def insertionSort(arr):
    n = len(arr)

    for i in range(n):
        j = i
        while (j > 0) and (arr[j-1] > arr[j]):
            arr[j - 1], arr[j] = arr[j], arr[j-1]
            j = j - 1
    return arr

# Solution 2:

