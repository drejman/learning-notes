"""
https://leetcode.com/problems/binary-search/
704. Binary Search

Given an array of integers nums which is sorted in ascending order, and an integer target,
write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1

Constraints:
1 <= nums.length <= 10^4
-10^4 < nums[i], target < 10^4
All the integers in nums are unique.
nums is sorted in ascending order.
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        input:
            nums: array sorted in ascending order
            target: value to find index of in array, might be missing
        output:
            index of found value
            -1 otherwise
        solution:
            bisect the interval
            compare value in the middle of interval to target
                if same return index
                if smaller choose first interval
                if bigger choose second interval
        example:
            1: 0, 5
                middle = (0 + 5) / 2 = 2.5
                take average of nums[2] and nums[3] -> 4
                compare: 9 > 4
                start = 3
            2: 3, 5
                middle = (3 + 5) / 2 = 4
                nums[4] -> 9
                compare: 9 = 9
                start = 4; end = 4

        example:
            nums = [-1,0,3,5,9,12], target = 5
            1: 0, 5
                middle = (0 + 5) / 2 = 2.5
                take average of nums[2] and nums[3] -> 4
                compare: 5 > 4
                start = 3
            2: 3, 5
                middle = (3 + 5) / 2 = 4
                nums[4] -> 9
                compare: 5 < 9
                end = 4
            3: 3, 4
                middle = 3.5
                average of nums[3] and nums[4] = 7
                compare: 5 < 7
                end = 3
        """
        start, end = 0, len(nums) - 1

        while start <= end:
            mid = (start + end) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1

        return -1

        # Solution using calculating median

        # import math
        # start, end = 0, len(nums) - 1
        # while start < end:
        #     midpoint = (start + end) / 2
        #     values = nums[math.floor(midpoint):math.ceil(midpoint)+1]
        #     median = sum(values) / len(values)
        #     if median == target:
        #         start = math.floor(midpoint)
        #         end = math.ceil(midpoint)
        #     elif median < target:
        #         start = math.ceil(midpoint)
        #     elif median > target:
        #         end = math.floor(midpoint)
        # if nums[start] == target:
        #     return start
        # return -1