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
Time Complexity

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
