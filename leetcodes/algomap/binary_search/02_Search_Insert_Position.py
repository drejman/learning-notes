"""
https://leetcode.com/problems/search-insert-position/
35. Search Insert Position

Given a sorted array of distinct integers and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4

Constraints:
1 <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4
nums contains distinct values sorted in ascending order.
-10^4 <= target <= 10^4
"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        input: sorted array (distinct values) and value to be inserted
        output: index where value should be inserted (or where it is if exists in array)
        Solution:
            binary search for target
            if not found return start
        Example:
            nums = [1,3,5,6], target = 2
            1:  s = 0, e = 3
                m = 1
                nums[1] -> 3 > 2
                e = 0
            2:  s = 0, e = 0
                m = 0
                nums[0] -> 1 < 2
                s = 1
            3:  s = 1 > e = 0
                return 1
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
        return start
