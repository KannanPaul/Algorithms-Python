'''
Merge sort

Input: ‘N’ = 7,
'ARR' = [2, 13, 4, 1, 3, 6, 28]

Output: [1 2 3 4 6 13 28]

Explanation: After applying 'merge sort' on the input array, the output is [1 2 3 4 6 13 28].

'''

# Solution 1:
'''
Time Complexity - O( N * logN ), where 'N' is the size of the array ‘arr’.

Merge Sort is a recursive algorithm. The time complexity of this algorithm can be calculated using the following expression: ‘T(n) = 2 * T(n / 2) + O(n)’.

After solving the above relation, the time complexity becomes ‘N * logN’.

Hence, the time complexity is O( N ).

Space Complexity - O( N ), where 'N' is the size of Array ‘arr’.

All elements are copied into a new array in the' merge' function.

Hence, the space complexity is O( N ).
'''

def mergeSort(array):
    if len(array) > 1:

        mid = len(array)//2
        L = array[:mid]
        R = array[mid:]

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0


        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = R[j]
                j += 1
            k += 1
          
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            array[k] = R[j]
            j += 1
            k += 1

array = [2, 13, 4, 1, 3, 6, 28]
mergeSort(array)
