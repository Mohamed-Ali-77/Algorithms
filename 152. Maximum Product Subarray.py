'''
Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.


Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

'''
#solution:
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        output = maxProd = minProd = nums[0]
        for n in nums[1:]:
            candidates = [n, maxProd*n, minProd*n]
            maxProd = max(candidates)
            minProd = min(candidates)
            output = max(output, maxProd)
        return output