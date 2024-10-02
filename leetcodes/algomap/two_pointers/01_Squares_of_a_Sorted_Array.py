"""
https://leetcode.com/problems/squares-of-a-sorted-array/
977. Squares of a Sorted Array

Given an integer array nums sorted in non-decreasing order,
return an array of the squares of each number sorted in non-decreasing order.

Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Example 2:
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]

Constraints:
1 <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4
nums is sorted in non-decreasing order.

Follow up: Squaring each element and sorting the new array is very trivial,
could you find an O(n) solution using a different approach?
"""


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        input: array of integers sorted in non-decreasing order
        output: array of the squares of each number in non-decresing order
        Solution:
            the input array consists of two subarrays:
                - negative values sorted in non-increasing order of absolute value
                - positive values sorted in non-decreasing order of absolute value
                (- and zeros between them)
            all of the orders are not the ones we want, so just reverse output at the end
            #1 create array of squares in non-increasing order (from the highest)
               it's easy because the highest absolute values will be at the ends of array
               so let's initialize two pointers at the ends and move towards middle,
               adding to the output array the one with the greater square
            Time: O(n)
            Space: O(n)
        """
        l, r = 0, len(nums) - 1
        squares = []
        sql, sqr = nums[l] ** 2, nums[r] ** 2  # calculate squares to compare ahead of time
        # kind of do-while loop
        while l < r:
            if sql > sqr:  # compare squares instead of absolute values
                squares.append(sql)
                l += 1
                sql = nums[l] ** 2  # so that we can recalculate each square only once
            else:
                squares.append(sqr)
                r -= 1
                sqr = nums[r] ** 2  # and do not perform any unnecessary operations

        # Add last square
        if sql > sqr:
            squares.append(sql)
        else:
            squares.append(sqr)
        return reversed(squares)
