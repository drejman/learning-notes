"""
https://leetcode.com/problems/product-of-array-except-self/
238. Product of Array Except Self

Given an integer array nums, return an array answer such that
answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:
2 <= nums.length <= 10^5
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

Follow up: Can you solve the problem in O(1) extra space complexity?
(The output array does not count as extra space for space complexity analysis.)
"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Input: array of numbers
        Output: array of numbers where i-th element is equalt to product(nums[:i]+nums[i+1:])
        Solution:
            each result is a product of two partial products
            - from the beggining to i
            - from i+1 to end
            need two sweeps for the table and incremental partial product,
            but we can keep partial product in output table
            time: O(n)
            space: O(1)
        Example:
        nums = [1, 2, 3, 4]
        prod_left[i] = prod_left[i+1] * nums[i+1]
        prod_left = [1, 1, 2, 6]

        prod_right[i] = prod_right[i-1] * nums[i-1]
        prod_right = [24, 12, 4, 1]

        output[i] = prod_left[i] * prod_right[i]
        output = [24, 12, 8, 6]
        """
        l = len(nums)
        output = [1] * l  # will be multiplyting, 1 is neutral element
        right_p = 1
        while right_p < l:
            output[right_p] = output[right_p - 1] * nums[right_p - 1]
            right_p += 1

        left_p = (l - 1) - 1
        prod_left = 1
        while left_p >= 0:
            prod_left *= nums[left_p + 1]
            output[left_p] *= prod_left
            left_p -= 1

        return output
