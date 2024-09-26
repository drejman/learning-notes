"""
https://leetcode.com/problems/find-closest-number-to-zero/description/
2239. Find Closest Number to Zero
Given an integer array nums of size n, return the number with the value closest to 0 in nums.
If there are multiple answers, return the number with the largest value.

Example 1:

Input: nums = [-4,-2,1,4,8]
Output: 1
Explanation:
The distance from -4 to 0 is |-4| = 4.
The distance from -2 to 0 is |-2| = 2.
The distance from 1 to 0 is |1| = 1.
The distance from 4 to 0 is |4| = 4.
The distance from 8 to 0 is |8| = 8.
Thus, the closest number to 0 in the array is 1.

Example 2:

Input: nums = [2,-1,1]
Output: 1
Explanation: 1 and -1 are both the closest numbers to 0, so 1 being larger is returned.

Constraints:

1 <= n <= 1000
-10^5 <= nums[i] <= 10^5
"""

class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        """
        Input: array of numbers
        Output: element from input that is
            a) closest to 0
            b) largest
        Solution:
            linear search through an array -> O(n) time
            keep the current best element and it's absolute value -> O(1) space
            calculate abs of current element and compare
            abs should be fast so no caching needed
            after iterating through whole array return best
        """
        value, abs_value = nums[0], abs(nums[0])
        for number in nums[1:]:
            abs_number = abs(number)
            if abs_number < abs_value:
                abs_value = abs_number
                value = number
            elif abs_number == abs_value:
                value = max(number, value)
        return value
