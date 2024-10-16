"""
https://leetcode.com/problems/majority-element/
169. Majority Element

Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2

Constraints:
n == nums.length
1 <= n <= 5 * 10^4
-10^9 <= nums[i] <= 10^9
Follow-up: Could you solve the problem in linear time and in O(1) space?
"""


class Solution:
    """
    Solution #1:
    Straightforward occurrence counting (using dict/hashmap), returning highest element with the highest count.

    Solution #2:
    Since majority element occurs always over half of the times, if we keep track of counts of one element,
    incrementing count for each occurrence and decrementing count for each other seen value,
    it will stay positive only for majority elements, for all other elements it would drop below 0.
    But keeping count below 0 would provide not any information about majority element
    (only which element is not majority), so once it drops to 0 it's time to change to a new candidate value.
    Even though number might be lined up in a way they will "cancel" the majority element several times,
    even in the worst case scenario count of majority element will be greater by one.
    """
    def majorityElement(self, nums: List[int]) -> int:
        # Solution #1 (using Counter)
        # from collections import Counter
        # counter = Counter(nums)
        # return counter.most_common(1)[0][0]

        # Solution #2 (by hand)
        # counter = {}
        # for num in nums:
        #     counter[num] = counter.get(num, 0) + 1

        # max_count = -1
        # ans = -1
        # for num, freq in counter.items():
        #     if freq > max_count:
        #         max_count = freq
        #         ans = num
        #
        # return ans

        # Solution #2:
        candidate = None
        count = 0

        for num in nums:
            if count == 0:  # time to change best guess to whatever else
                candidate = num

            count += 1 if candidate == num else -1  # increment if matches current best guess else decrement

        return candidate
