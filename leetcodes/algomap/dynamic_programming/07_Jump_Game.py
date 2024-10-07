"""
https://leetcode.com/problems/jump-game/description/
55. Jump Game
You are given an integer array nums. You are initially positioned at the array's first index,
and each element in the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.

Example 1:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what.
Its maximum jump length is 0, which makes it impossible to reach the last index.

Constraints:
1 <= nums.length <= 10^4
0 <= nums[i] <= 10^5
"""


class Solution:
    """
    Solution:
        Dynamic Programming:
            Recursive:
                if can reach from current to the end then return yes
                else call every possible jump length
                return any(results)
                Time: O(Max(nums) ^ n)
	            Space: O(n)
            Top-down (Memoization):
                set initial point as reachable
                mark all reachable as reachable
                continue for each reachable point
                Time: O(n^2)
                Space: O(n)
            Greedy:
                start from the end
                set end as target
                iterate from the last towards beginning
                check if can reach target from current index (with max)
                    - if yes change target to current index
                    - if no then continue
                Time: O(n)
                Space: O(1)
    """

    def canJump(self, nums: List[int]) -> bool:
        end = len(nums) - 1

        # Recursive fails time, so slapped LRU cache on that and worked
        # from functools import cache
        # @cache
        # def is_possible_to_reach(current: int) -> bool:
        #     max_jump = nums[current]
        #     if end - current <= max_jump:
        #         return True
        #     if max_jump == 0:
        #         return False
        #     return any([is_possible_to_reach(current + i) for i in range(1, max_jump+1)])

        # return is_possible_to_reach(0)

        # end_reachable_from = {end: True}  # end is reachable from end

        # DP with memoization (fails time)
        # def can_reach(i: int) -> bool:
        #     if i in end_reachable_from:
        #         return end_reachable_from[i]

        #     for step in range(1, nums[i]+1):
        #         if can_reach(i+step):
        #             end_reachable_from[i] = True
        #             return True

        #     end_reachable_from[i] = False
        #     return False

        # return can_reach(0)

        # Greedy
        target = end
        for i in range(end, -1, -1):
            if i >= target:
                continue
            if i + nums[i] >= target:
                # if target is reachable from current,
                # change to subproblem reaching new target from earlier indices
                target = min(target, i)
        return target == 0
