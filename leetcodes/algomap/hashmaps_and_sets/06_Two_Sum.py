"""
https://leetcode.com/problems/two-sum/
1. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
2 <= nums.length <= 10^4
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9
Only one valid answer exists.

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Input: array of integers; target value
        Output: indices of two number that add to target
        Solution:
            create a lookup number: index
                + time: O(n)
                + space: O(n)
            for each element check if complementing value exists
                if yes return
                if not continue
                + time: O(n)
                + space: none
        """
        lookup = {value: index for index, value in enumerate(nums)}
        for index, value in enumerate(nums):
            complement = target - value
            index_compl = lookup.get(complement)
            if index_compl and index_compl != index:
                return [index, index_compl]