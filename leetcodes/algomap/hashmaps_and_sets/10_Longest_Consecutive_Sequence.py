"""
https://leetcode.com/problems/longest-consecutive-sequence/
128. Longest Consecutive Sequence

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4

Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Constraints:
0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
"""


class Solution:
    """
    Observation:
    Every initial number in a sequence does not have a preceding number in the array.
    Therefore, it's enough to, for every number that is a beginning of a sequence,
    check how long the sequence is (i.e. how long the subsequent number exists in the array).

    Solution:
    As there will be many checks of whether number exists in an input, use set (hashset) for O(1) "in" operation.
    1. Create a set of numbers
    2. For every number
    a) check if it is a beginning of a sequence
    b) if yes, keep count of how many number is in that sequence
    c) return highest count

    Time: O(n)
    Space: O(n)
    """
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0
        for num in nums:
            if (num - 1) not in nums:
                length = 1
                next_num = num + 1
                while next_num in nums:
                    length += 1
                    next_num += 1
                longest = max(longest, length)
        return longest
