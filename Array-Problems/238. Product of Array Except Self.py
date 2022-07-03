'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
'''

#solution:
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix,suffix = [1]*len(nums) , [1]*len(nums)
        answer = []
        pre ,suf= 1 ,1
        
        for i in range(len(nums)-1):
            pre = pre * nums[i]
            prefix[i+1] = pre
            suf = suf * nums[-1-i]
            suffix[-2-i] = suf
        for i in range(len(nums)):
            answer.append(prefix[i]*suffix[i])
        return answer
        