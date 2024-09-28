"""
https://leetcode.com/problems/3sum/submissions/1405423222/
15. 3 Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

Constraints:
3 <= nums.length <= 3000
-10^5 <= nums[i] <= 10^5
"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Input: possible members of correct triplet, not sorted, not unique
                each number (index) can be used only once
        Output: all correct, distinct triplets (no duplicates) in any order
        Solution #1 Two Pointers:
            triplet must sum to 0
            sort the array: O(nlogn)
            for each unique element n:  # O(n)
                find two elements with given sum (-n) -> high low pointers
                move one of the pointers to next different value
            because sum is 0 then either:
                - all are 0
                - some are negative and some are positive
                    + therefore is we are moving from lowest to highest we can stop at 0+
            Time: O(n^2)
            Space: O(1)

        Solution #2:
            create a lookup (hashmap)
        """
        result = []
        nums.sort()
        n = len(nums)
        prev_value = None
        for index, value in enumerate(nums):
            if value > 0:
                break
            if value == prev_value:
                continue
            prev_value = value
            low, high = index + 1, n - 1
            while low < high:
                sum_ = value + nums[low] + nums[high]
                if sum_ == 0:
                    result.append([value, nums[low], nums[high]])
                    # move both
                    low += 1
                    high -= 1
                    # skip repeated values
                    while low < high and nums[low] == nums[low - 1]:
                        low += 1
                    while low < high and nums[high] == nums[high + 1]:
                        high -= 1
                elif sum_ < 0:
                    low += 1
                else:  # sum_ > 0
                    high -= 1
        return result

        # from collections import Counter
        #
        # counter = Counter(nums)
        # s = set()
        #
        # for i in counter.keys():
        #     for j in counter.keys():
        #         if j == i and counter[j] < 2:
        #             continue
        #         desired = - (i + j)
        #         if desired in counter:
        #             needed_count = 1
        #             if desired == i:
        #                 needed_count += 1
        #             if desired == j:
        #                 needed_count += 1
        #             if counter[desired] < needed_count:
        #                 continue
        #             s.add(tuple(sorted([i, j, desired])))
        # return s