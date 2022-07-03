'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.


Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

'''
#solution:
class Solution:
    def threeSum(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        res = []
        for i in range(len(arr)):
            if i > 0 and arr[i] == arr[i-1]:
                continue
            target = -arr[i]
            left, right = i+1, len(arr)-1
            while left < right:
                if arr[left] + arr[right] == target:
                    res.append([arr[i], arr[left], arr[right]])
                    left +=1
                    while arr[left] == arr [left -1] and left < right:
                        left +=1
                elif arr[left] + arr[right] < target:
                    left += 1
                else:
                    right -= 1
        return res