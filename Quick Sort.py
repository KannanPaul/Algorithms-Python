'''
 Problem statement

Given the 'start' and the 'end'' positions of the array 'input'. Your task is to sort the elements between 'start' and 'end' using quick sort.


Note :

Make changes in the input array itself.

Detailed explanation ( Input/output format, Notes, Images )
Sample Input 1 :

6 
2 6 8 5 4 3

Sample Output 1 :

2 3 4 5 6 8

Sample Input 2 :

5
1 2 3 5 7

Sample Output 2 :

1 2 3 5 7 

Constraints :

1 <= N <= 10^3
0 <= input[i] <= 10^9

'''


#### Solution 1: Always pick the last element as a pivot 

def parition(arr, low, high):
    pivot = arr[high]

    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1



def quickSort(arr: List[int], startIndex: int, endIndex: int):
    """
    Don't write main().
    Don't read input, it is passed as function argument.
    Change in the given array itself.
    Taking input and printing output is handled automatically.
    """
    if startIndex < endIndex:
        pi = parition(arr, startIndex, endIndex)

        quickSort(arr, startIndex, pi-1)
        quickSort(arr, pi+1, endIndex)


'''
Time Complexity

O(‘N’ * log(‘N’)), Where ‘N’ is the length of the array.

If the pivot is the smallest or the largest number in the range, then it is not a good partition. In that case (the worst case), the time complexity will be O('N' ^ 2), because the time complexity of the partition function is O('N') and it is called ‘N’ times.

The best partition is when the pivot is the middle element. In that case, the partition function is called log('N') times. Therefore, the best case time complexity is O('N' * log('N')).

In an average case, generally, the partition is not that extreme, so the time complexity is same as the best case.

Hence the time complexity is O(‘N’ * log(‘N’)).
Space Complexity

O(log(‘N’)), Where ‘N’ is the length of the array.

The partition function is called log(‘N’) times (in average). So the recursion call stack takes log('N') space.

Hence the space complexity is O(log(‘N’)).
'''


#### Solution 2:  middle element to be the pivot.

def partition(arr, low, high):
    pivot = arr[(low + high) // 2]  # Choosing the middle element as the pivot
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while arr[i] < pivot:
            i += 1

        j -= 1
        while arr[j] > pivot:
            j -= 1

        if i >= j:
            return j

        arr[i], arr[j] = arr[j], arr[i]


def quick_sort(arr):
    def _quick_sort(items, low, high):
        if low < high:
            partition_index = partition(items, low, high)
            _quick_sort(items, low, partition_index)
            _quick_sort(items, partition_index + 1, high)

    _quick_sort(arr, 0, len(arr) - 1)


# Example usage:
arr = [29, 10, 14, 37, 13]
quick_sort(arr)
print("Sorted array:", arr)


#### Solution 3:  picking the first element as the Pivot:
def partition(arr,low, high):
    pivot = arr[low]
    i = low+1
    j = high
    
    while True:
        while i<= j and arr[i] <= pivot:
            i += 1
            
        while i<= j and arr[j] >= pivot:
            j -=1
        
        if i >= j:
            arr[low], arr[j] = arr[j], arr[low]
            return j
        
        arr[i], arr[j] = arr[j], arr[i]

def quick_sort(arr, start, end):
    if start < end:
        pi = partition(arr,start, end)
        quick_sort(arr, start, pi-1)
        quick_sort(arr, pi+1, end)
