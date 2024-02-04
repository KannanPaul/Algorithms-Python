'''
Problem statement
Sort the given unsorted array 'arr' of size 'N' in non-decreasing order using the selection sort algorithm.

 Note:
Change in the input array/list itself. 

Example:
Input:
N = 5
arr = {8, 6, 2, 5, 1}

Output:
1 2 5 6 8 

Sample Input 1:

6
2 13 4 1 3 6 

Sample Output 1:

1 2 3 4 6 13 
'''

# Solution 1:
'''
# Approach: The selection sort algorithm works by repeatedly selecting the smallest element from the unsorted part of the array and moving it to the beginning of the unsorted part. This process is done iteratively until the entire array is sorted.

# Time Complexity

O(N^2), where ‘N’ is the number of length of array.

The algorithm consists of two nested loops. The outer loop runs n-1 times, as it iterates from the first element to the second-to-last element of the array. The inner loop runs from i+1 to n-1, which is also approximately n iterations on average.

Therefore, the total number of comparisons and updates performed by the algorithm is approximately (n-1) + (n-2) + ... + 1, which is equal to (n * (n-1)) / 2. This gives us the time complexity of O(n^2) for the selection sort algorithm.

Space Complexity

O(1)

Reference link - https://www.programiz.com/dsa/selection-sort
'''

def selectionSort(arr: List[int]) -> None: 
    # Write your code here
    n = len(arr)
    for i in range(n):
        min = i
        for j in range(i+1, n):
            if arr[j] < arr[min]:
                min = j
        arr[min], arr[i] = arr[i], arr[min] 
        
    return arr

# Solution 2: Recusrion Insertion Sort
# Time Complexity: O(n2)
# Auxiliary Space: O(n)
# Reference - https://www.geeksforgeeks.org/recursive-selection-sort/?ref=lbp

def minIndex( a , i , j ):
	if i == j:
	   return i
	k = minIndex(a, i + 1, j)
	
	return (i if a[i] < a[k] else k)

def recurSelectionSort(a, n, index = 0):

	if index == n:
	   return -1
		
	
	k = minIndex(a, index, n-1)
	
	
	if k != index:
	   a[k], a[index] = a[index], a[k]
	
	recurSelectionSort(a, n, index + 1)
	

arr = [3, 1, 5, 2, 7, 0]
n = len(arr)

recurSelectionSort(arr, n)


