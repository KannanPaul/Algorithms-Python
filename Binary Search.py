'''
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. 
If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
'''

#Solution-1 - Timecomplexity -O(log n)
#Iterative Method
def binarysearch(nums,target,low,high):
  while low<=high:
    mid=(low+high)//2
    if target== nums[mid]:
        return mid
    elif nums[mid] <target:
        low=mid+1
    else:
        high=mid-1
  return -1
        
nums = [-1,0,3,5,9,12]
target = 9
print(binarysearch(nums,target,0,len(nums)-1))


#Solution-2
#Recursive Method
def binarysearch(a,target,low,high):
  if low<=high:
    mid=(low+high)//2
    if target==a[mid]:
       return mid
    elif a[mid] < target:
       return binarysearch(a,target,mid+1,high)
    else:
      return binarysearch(a,target,low,mid-1)
  else:
    return -1

nums = [-1,0,3,5,9,12]
target = 9
print(binarysearch(nums,target,0,len(nums)-1))
